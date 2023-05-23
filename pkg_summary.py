import argparse
from conans.client import conan_api
import pprint

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('recipe_name', type=str, help='The recipe to be searched, e.g. protobuf')
    parser.add_argument('--debug', action='store_true', help='Verbose mode')
    parser.add_argument('--noptions', nargs='+', help="List the option names: shared")
    parser.add_argument('--nsettings', nargs='+', help="List the settings names: os arch, compiler")
    parser.add_argument("--remote", required=False, type=str, default="all", help='The remote to be searched')
    args = parser.parse_args()
    print ("Remote to be searched:", args.remote)
    print ("Selected options:", args.noptions)
    print ("Selected settings:", args.nsettings)
    conan, _, _ = conan_api.Conan.factory()
    recipes = conan.search_recipes(pattern=args.recipe_name,remote_name=args.remote)
    for recipe in recipes["results"][0]["items"]:
        if args.debug:
            print ("Recipe data:")
            pprint.pprint(recipe)
        recipe_id = recipe["recipe"]["id"]
        packages = None
        try:
            packages = conan.search_packages(recipe_id, remote_name=args.remote)
        except:
            continue
        if packages == None:
            continue
        if args.debug:
            print ("Packages data:")
            pprint.pprint(packages)
        if len(packages["results"]) < 1:
            continue

        recipe_remote = ""
        if "remote" in packages["results"][0]:
            recipe_remote = packages["results"][0]["remote"]
        print (" recipe id:", recipe_id, recipe_remote, len(packages["results"][0]["items"][0]["packages"]))
        # for all packages of this recipe, and print the requested fields
        for package in packages["results"][0]["items"][0]["packages"]:
            if args.debug:
                pprint.pprint(package)
            package_id = package["id"]
            line = package_id + " "
            for o in args.noptions:
                if o in package["options"]:
                    line += package["options"][o] + " "
            for s in args.nsettings:
                if s in package["settings"]:
                    line += package["settings"][s] + " "
            print (line)


