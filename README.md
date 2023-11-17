## PHP Vulnerability Scanner

This Python script is designed to scan a list of domains for potential PHP vulnerability using PHPUnit's eval-stdin.php file. It checks for specific strings indicating vulnerability and saves the vulnerable URLs to a file.

### How It Works

The script takes a file containing a list of domains and the number of threads to use for scanning.

### Usage

```bash
python scanner.py <file_with_domains> <num_threads>
