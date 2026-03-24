#!/usr/bin/env python3
"""
Professional Folder Tree Generator
A comprehensive tool for generating beautiful folder structure visualizations
Compatible with Python 3.7+
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple
from datetime import datetime
import json

# For image generation
try:
    from PIL import Image, ImageDraw, ImageFont
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

# For PDF generation
try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False

class FileTypeIcons:
    """File type icons - emoji for artisanal, fallback symbols for compatibility"""

    # Artisanal icon set with beautiful emojis (with fallbacks for compatibility)
    ARTISANAL = {
        # Documents
        '.txt': '📄', '.md': '📝', '.pdf': '📄', '.doc': '📃', '.docx': '📃',
        '.rtf': '📄', '.odt': '📄', '.pages': '📄',

        # Spreadsheets and Data
        '.xls': '📊', '.xlsx': '📊', '.csv': '📊', '.ods': '📊',

        # Presentations
        '.ppt': '📊', '.pptx': '📊', '.odp': '📊', '.key': '📊',

        # Images
        '.jpg': '🖼️', '.jpeg': '🖼️', '.png': '🖼️', '.gif': '🖼️', '.bmp': '🖼️',
        '.svg': '🎨', '.ico': '🖼️', '.tiff': '🖼️', '.webp': '🖼️',

        # Audio
        '.mp3': '🎵', '.wav': '🎵', '.flac': '🎵', '.aac': '🎵', '.ogg': '🎵',
        '.m4a': '🎵', '.wma': '🎵',

        # Video
        '.mp4': '🎬', '.avi': '🎬', '.mkv': '🎬', '.mov': '🎬', '.wmv': '🎬',
        '.flv': '🎬', '.webm': '🎬', '.m4v': '🎬',

        # Code files
        '.py': '🐍', '.js': '📜', '.html': '🌐', '.css': '🎨', '.php': '🐘',
        '.java': '☕', '.cpp': '⚙️', '.c': '⚙️', '.cs': '🔷', '.rb': '💎',
        '.go': '🐹', '.rs': '🦀', '.swift': '🐦', '.kt': '🅺', '.scala': '⚖️',
        '.r': '📈', '.sql': '🗄️', '.sh': '💻', '.bat': '⚙️', '.ps1': '💻',

        # Special files
        '.ipynb': '📓', '.json': '🔧', '.yml': '🔧', '.yaml': '🔧',
        '.xml': '🔧', '.ini': '🔧', '.conf': '🔧', '.config': '🔧', '.toml': '🔧',

        # Archives
        '.zip': '🗜️', '.rar': '🗜️', '.7z': '🗜️', '.tar': '🗜️', '.gz': '🗜️',
        '.bz2': '🗜️', '.xz': '🗜️',

        # Executables
        '.exe': '⚙️', '.msi': '📦', '.deb': '📦', '.rpm': '📦', '.dmg': '📦',
        '.app': '📱', '.apk': '📱',

        # Default icons
        'folder': '📁', 'key_folder': '📂', 'file': '📄', 'unknown': '❓'
    }

    # Simple icon set (basic ASCII-safe symbols)
    SIMPLE = {
        '.txt': 'T', '.md': 'M', '.pdf': 'P', '.doc': 'D', '.docx': 'D',
        '.jpg': 'I', '.jpeg': 'I', '.png': 'I', '.gif': 'G', '.svg': 'S',
        '.mp3': 'A', '.wav': 'A', '.mp4': 'V', '.avi': 'V',
        '.py': 'P', '.js': 'J', '.html': 'H', '.css': 'C',
        '.zip': 'Z', '.rar': 'R',
        'folder': '+', 'file': '-', 'unknown': '?'
    }

    # Professional icon set (clean brackets with type indicators)
    PROFESSIONAL = {
        '.txt': '[TXT]', '.md': '[MD]', '.pdf': '[PDF]', '.doc': '[DOC]', '.docx': '[DOC]',
        '.xls': '[XLS]', '.xlsx': '[XLS]', '.csv': '[CSV]',
        '.jpg': '[IMG]', '.jpeg': '[IMG]', '.png': '[IMG]', '.gif': '[GIF]',
        '.mp3': '[MP3]', '.wav': '[WAV]', '.mp4': '[MP4]', '.avi': '[AVI]',
        '.py': '[PY]', '.js': '[JS]', '.html': '[HTM]', '.css': '[CSS]',
        '.zip': '[ZIP]', '.rar': '[RAR]',
        'folder': '[DIR]', 'file': '[   ]', 'unknown': '[?]'
    }

class TreeStyle:
    """Tree drawing styles with improved alignment"""

    STYLES = {
        'simple': {
            'vertical': '│ ',
            'horizontal': '─ ',
            'junction': '├─ ',
            'corner': '└─ ',
            'space': '  '
        },
        'professional': {
            'vertical': '│ ',
            'horizontal': '─ ',
            'junction': '├─ ',
            'corner': '└─ ',
            'space': '  '
        },
        'artisanal': {
            'vertical': '│ ',
            'horizontal': '─ ',
            'junction': '├─ ',
            'corner': '└─ ',
            'space': '  '
        },
        'ascii': {
            'vertical': '| ',
            'horizontal': '- ',
            'junction': '+- ',
            'corner': '+- ',
            'space': '  '
        }
    }

class FolderTreeGenerator:
    """Professional folder tree generator with multiple output formats"""

    def __init__(self, style='simple', icon_set='simple', max_depth=3, max_files_per_folder=None):
        self.style = TreeStyle.STYLES.get(style, TreeStyle.STYLES['simple'])
        self.icon_set = getattr(FileTypeIcons, icon_set.upper(), FileTypeIcons.SIMPLE)
        self.max_depth = max_depth
        self.max_files_per_folder = max_files_per_folder
        self.tree_lines = []
        self.stats = {'folders': 0, 'files': 0, 'total_size': 0, 'truncated_folders': 0}

        # File type categories for filtering
        self.file_categories = {
            'documents': {'.txt', '.md', '.pdf', '.doc', '.docx', '.rtf', '.odt'},
            'images': {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico', '.tiff', '.webp'},
            'audio': {'.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma'},
            'video': {'.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'},
            'code': {'.py', '.js', '.html', '.css', '.php', '.java', '.cpp', '.c', '.cs', '.rb'},
            'archives': {'.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'},
        }

    def get_file_icon(self, file_path: Path, is_key_folder: bool = False) -> str:
        """Get icon for file based on extension"""
        if file_path.is_dir():
            if is_key_folder:
                return self.icon_set.get('key_folder', '📂')
            return self.icon_set.get('folder', '📁')

        ext = file_path.suffix.lower()
        return self.icon_set.get(ext, self.icon_set.get('file', '📄'))

    def is_key_directory(self, dir_name: str) -> bool:
        """Determine if directory is a key project directory"""
        key_dirs = {
            'src', 'source', 'lib', 'libs', 'app', 'apps', 'components',
            'pages', 'views', 'models', 'controllers', 'services', 'utils',
            'helpers', 'config', 'configs', 'settings', 'static', 'assets',
            'resources', 'public', 'private', 'data', 'database', 'db',
            'migrations', 'schemas', 'api', 'apis', 'routes', 'middleware',
            'templates', 'views', 'layouts', 'partials', 'includes',
            'tests', 'test', 'spec', 'specs', 'docs', 'documentation',
            'examples', 'samples', 'demos', 'tutorials', 'guides',
            'scripts', 'tools', 'bin', 'build', 'dist', 'output',
            'notebooks', 'helpfiles'
        }
        return dir_name.lower() in key_dirs

    def get_file_size(self, file_path: Path) -> int:
        """Get file size safely"""
        try:
            return file_path.stat().st_size if file_path.is_file() else 0
        except (OSError, PermissionError):
            return 0

    def format_size(self, size_bytes: int) -> str:
        """Format file size in human readable format"""
        if size_bytes == 0:
            return "0 B"

        size_names = ["B", "KB", "MB", "GB", "TB"]
        i = 0
        while size_bytes >= 1024 and i < len(size_names) - 1:
            size_bytes /= 1024.0
            i += 1

        return f"{size_bytes:.1f} {size_names[i]}"

    def should_include_file(self, file_path: Path, include_categories: Optional[Set[str]] = None,
                           exclude_patterns: Optional[Set[str]] = None) -> bool:
        """Check if file should be included based on filters"""
        if exclude_patterns:
            for pattern in exclude_patterns:
                if pattern in file_path.name:
                    return False

        if include_categories and not file_path.is_dir():
            ext = file_path.suffix.lower()
            for category in include_categories:
                if ext in self.file_categories.get(category, set()):
                    return True
            return False

        return True

    def generate_tree(self, root_path: str, show_size: bool = False,
                     show_hidden: bool = False, sort_dirs_first: bool = True,
                     include_categories: Optional[Set[str]] = None,
                     exclude_patterns: Optional[Set[str]] = None) -> List[str]:
        """Generate tree structure as list of strings"""
        self.tree_lines = []
        self.stats = {'folders': 0, 'files': 0, 'total_size': 0, 'truncated_folders': 0}

        root = Path(root_path).resolve()
        if not root.exists():
            raise FileNotFoundError(f"Path does not exist: {root_path}")

        # Add root directory
        root_icon = self.get_file_icon(root, is_key_folder=True)
        root_line = f"{root_icon} {root.name}/"
        if show_size and root.is_dir():
            try:
                total_size = sum(f.stat().st_size for f in root.rglob('*') if f.is_file())
                root_line += f" ({self.format_size(total_size)})"
            except (OSError, PermissionError):
                pass

        self.tree_lines.append(root_line)
        self.stats['folders'] += 1

        # Generate tree recursively
        self._build_tree(root, "", 0, show_size, show_hidden, sort_dirs_first,
                        include_categories, exclude_patterns)

        return self.tree_lines

    def _build_tree(self, directory: Path, prefix: str, depth: int, show_size: bool,
                   show_hidden: bool, sort_dirs_first: bool, include_categories: Optional[Set[str]],
                   exclude_patterns: Optional[Set[str]]) -> None:
        """Recursively build tree structure with smart file limiting"""
        if depth >= self.max_depth:
            return

        try:
            entries = list(directory.iterdir())
        except (OSError, PermissionError):
            return

        # Filter entries
        if not show_hidden:
            entries = [e for e in entries if not e.name.startswith('.')]

        entries = [e for e in entries if self.should_include_file(e, include_categories, exclude_patterns)]

        # Sort entries
        if sort_dirs_first:
            entries.sort(key=lambda x: (x.is_file(), x.name.lower()))
        else:
            entries.sort(key=lambda x: x.name.lower())

        # Smart file limiting: separate directories and files
        directories = [e for e in entries if e.is_dir()]
        files = [e for e in entries if e.is_file()]

        # Apply file limit if specified
        files_truncated = False
        if self.max_files_per_folder and len(files) > self.max_files_per_folder:
            displayed_files = files[:self.max_files_per_folder]
            hidden_count = len(files) - self.max_files_per_folder
            files_truncated = True
            self.stats['truncated_folders'] += 1
        else:
            displayed_files = files
            hidden_count = 0

        # Combine directories (always show all) with limited files
        entries_to_show = directories + displayed_files

        for i, entry in enumerate(entries_to_show):
            is_last_entry = i == len(entries_to_show) - 1 and not files_truncated

            # Build tree symbols with better spacing
            if is_last_entry:
                current_prefix = prefix + self.style['corner']
                next_prefix = prefix + self.style['space']
            else:
                current_prefix = prefix + self.style['junction']
                next_prefix = prefix + self.style['vertical']

            # Get icon and build line
            is_key = self.is_key_directory(entry.name) if entry.is_dir() else False
            icon = self.get_file_icon(entry, is_key_folder=is_key)
            line = f"{current_prefix}{icon} {entry.name}"

            if entry.is_dir():
                line += "/"
                self.stats['folders'] += 1
            else:
                self.stats['files'] += 1
                file_size = self.get_file_size(entry)
                self.stats['total_size'] += file_size

                if show_size:
                    line += f" ({self.format_size(file_size)})"

            self.tree_lines.append(line)

            # Recurse into directories
            if entry.is_dir():
                self._build_tree(entry, next_prefix, depth + 1, show_size, show_hidden,
                               sort_dirs_first, include_categories, exclude_patterns)

        # Add truncation indicator if files were hidden
        if files_truncated:
            truncation_prefix = prefix + self.style['corner'] if len(entries_to_show) > 0 else prefix + self.style['junction']
            truncation_line = f"{truncation_prefix}... ({hidden_count} more files)"
            self.tree_lines.append(truncation_line)

    def save_text(self, output_path: str, header: bool = True, root_path: str = "") -> None:
        """Save tree as text file with beautiful header"""
        with open(output_path, 'w', encoding='utf-8') as f:
            if header:
                # Beautiful header like the original
                project_name = Path(root_path).name if root_path else "Project"
                f.write(f"{project_name.upper()} Project Tree Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Root: {root_path}\n")
                f.write("(c) 2024 Hans Hendrickx - MIT License\n")
                f.write("Professional Folder Tree Generator\n\n")

                f.write("Project Structure Legend:\n")
                f.write("📂 - Key Project Directory\n")
                f.write("📁 - Regular Directory\n")
                f.write("🐍 - Python Source File\n")
                f.write("📓 - Jupyter Notebook\n")
                f.write("📝 - Markdown File\n")
                f.write("📊 - Excel or CSV File\n")
                f.write("📄 - PDF File\n")
                f.write("📃 - Word Document\n")
                f.write("⚙️ - Batch/Script File\n")
                f.write("🔧 - JSON or Config File\n")
                f.write("🖼️ - Image File\n")
                f.write("🎵 - Audio File\n")
                f.write("🎬 - Video File\n")
                f.write("-" * 80 + "\n\n")

            for line in self.tree_lines:
                f.write(line + "\n")

            if header:
                f.write(f"\n" + "-" * 80 + "\n")
                f.write(f"Total Folders: {self.stats['folders']}\n")
                f.write(f"Total Files: {self.stats['files']}\n")
                f.write(f"Total Size: {self.format_size(self.stats['total_size'])}\n")

    def save_png(self, output_path: str, font_size: int = 12) -> None:
        """Save tree as PNG image"""
        if not PIL_AVAILABLE:
            raise ImportError("PIL (Pillow) is required for PNG output. Install with: pip install Pillow")

        # Calculate image dimensions
        max_line_length = max(len(line) for line in self.tree_lines) if self.tree_lines else 50
        line_height = font_size + 4
        img_width = max(800, max_line_length * (font_size // 2))
        img_height = max(600, len(self.tree_lines) * line_height + 100)

        # Create image
        img = Image.new('RGB', (img_width, img_height), color='white')
        draw = ImageDraw.Draw(img)

        # Try to load a font
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except OSError:
            try:
                font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", font_size)
            except OSError:
                font = ImageFont.load_default()

        # Draw header
        y_offset = 20
        header_text = [
            f"Folder Tree - Generated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Folders: {self.stats['folders']} | Files: {self.stats['files']} | Size: {self.format_size(self.stats['total_size'])}"
        ]

        for header_line in header_text:
            draw.text((20, y_offset), header_line, fill='black', font=font)
            y_offset += line_height

        y_offset += 10

        # Draw tree lines
        for line in self.tree_lines:
            draw.text((20, y_offset), line, fill='black', font=font)
            y_offset += line_height

        img.save(output_path)

    def save_pdf(self, output_path: str, page_size='A4') -> None:
        """Save tree as PDF"""
        if not REPORTLAB_AVAILABLE:
            raise ImportError("ReportLab is required for PDF output. Install with: pip install reportlab")

        page_size_map = {'A4': A4, 'letter': letter}
        page_width, page_height = page_size_map.get(page_size, A4)

        c = canvas.Canvas(output_path, pagesize=(page_width, page_height))

        # Set up fonts and spacing
        font_name = "Helvetica"
        font_size = 10
        line_height = font_size + 2
        margin = 50

        # Title and header
        c.setFont(font_name, 14)
        y_position = page_height - margin
        c.drawString(margin, y_position, "Folder Tree Report")

        y_position -= 30
        c.setFont(font_name, 10)
        c.drawString(margin, y_position, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        y_position -= line_height
        c.drawString(margin, y_position, f"Folders: {self.stats['folders']} | Files: {self.stats['files']} | Total Size: {self.format_size(self.stats['total_size'])}")

        y_position -= 30

        # Tree content
        c.setFont(font_name, 8)
        for line in self.tree_lines:
            if y_position < margin:
                c.showPage()
                y_position = page_height - margin
                c.setFont(font_name, 8)

            c.drawString(margin, y_position, line)
            y_position -= line_height

        c.save()

def main():
    """Main function with argument parsing"""
    parser = argparse.ArgumentParser(
        description="Professional Folder Tree Generator - Create beautiful folder structure visualizations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s /path/to/folder                                    # Simple console output
  %(prog)s /path/to/folder -o tree.png                        # PNG output
  %(prog)s /path/to/folder --formats all                      # Generate TXT, PNG, and PDF
  %(prog)s /path/to/folder --formats txt png --output-prefix my_project  # Generate TXT and PNG
  %(prog)s /path/to/folder --style artisanal --depth 5        # Detailed tree, 5 levels deep
  %(prog)s /path/to/folder --include-categories code images   # Only code and image files
  %(prog)s /path/to/folder --max-files 5                      # Perfect for A4 documentation
        """
    )

    parser.add_argument('path', help='Path to the folder to analyze')
    parser.add_argument('-o', '--output', help='Output file (extension determines format: .txt, .png, .pdf)')
    parser.add_argument('--style', choices=['simple', 'professional', 'artisanal'],
                       default='simple', help='Tree drawing style')
    parser.add_argument('--icons', choices=['simple', 'professional', 'artisanal'],
                       default='simple', help='Icon set to use')
    parser.add_argument('--depth', type=int, choices=range(1, 11), default=3,
                       help='Maximum depth to traverse (1-10)')
    parser.add_argument('--show-size', action='store_true',
                       help='Show file sizes')
    parser.add_argument('--show-hidden', action='store_true',
                       help='Include hidden files and folders')
    parser.add_argument('--no-sort-dirs', action='store_true',
                       help='Don\'t sort directories first')
    parser.add_argument('--include-categories', nargs='+',
                       choices=['documents', 'images', 'audio', 'video', 'code', 'archives'],
                       help='Only include specific file categories')
    parser.add_argument('--exclude-patterns', nargs='+',
                       help='Exclude files/folders containing these patterns')
    parser.add_argument('--formats', nargs='+', choices=['txt', 'png', 'pdf', 'all'],
                       default=None, help='Output formats to generate (txt, png, pdf, all). Use with --output-prefix')
    parser.add_argument('--output-prefix', default='folder_tree',
                       help='Prefix for output files when using --formats (default: folder_tree)')
    parser.add_argument('--max-files', type=int, default=None,
                       help='Maximum files to show per folder (default: unlimited, recommended: 5-10 for A4)')
    parser.add_argument('--font-size', type=int, default=12,
                       help='Font size for PNG output (default: 12)')
    parser.add_argument('--page-size', choices=['A4', 'letter'], default='A4',
                       help='Page size for PDF output')
    parser.add_argument('--version', action='version', version='%(prog)s 2.0')

    args = parser.parse_args()

    # Validate path
    if not os.path.exists(args.path):
        print(f"Error: Path '{args.path}' does not exist.")
        sys.exit(1)

    # Create generator
    generator = FolderTreeGenerator(
        style=args.style,
        icon_set=args.icons,
        max_depth=args.depth,
        max_files_per_folder=args.max_files
    )

    try:
        # Generate tree
        print("Generating folder tree...")
        tree_lines = generator.generate_tree(
            args.path,
            show_size=args.show_size,
            show_hidden=args.show_hidden,
            sort_dirs_first=not args.no_sort_dirs,
            include_categories=set(args.include_categories) if args.include_categories else None,
            exclude_patterns=set(args.exclude_patterns) if args.exclude_patterns else None
        )

        # Determine output format and save
        if args.output:
            output_path = Path(args.output)
            ext = output_path.suffix.lower()

            if ext == '.png':
                generator.save_png(args.output, font_size=args.font_size)
                print(f"Tree saved as PNG: {args.output}")
            elif ext == '.pdf':
                generator.save_pdf(args.output, page_size=args.page_size)
                print(f"Tree saved as PDF: {args.output}")
            else:  # Default to text
                generator.save_text(args.output)
                print(f"Tree saved as text: {args.output}")
        else:
            # Print to console
            for line in tree_lines:
                print(line)

        # Print statistics
        print(f"\nStatistics:")
        print(f"  Folders: {generator.stats['folders']}")
        print(f"  Files: {generator.stats['files']}")
        print(f"  Total Size: {generator.format_size(generator.stats['total_size'])}")
        if generator.stats['truncated_folders'] > 0:
            print(f"  Folders with truncated file lists: {generator.stats['truncated_folders']}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()