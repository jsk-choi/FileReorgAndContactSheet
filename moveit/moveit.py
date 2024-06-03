import os
import shutil

destination_dirs = ["Q:\\00", "Q:\\00\\_ tg"]
source_dir = "Q:\\zz-org"
stage_dir = "Q:\\00\\__from__"

destinations = []
source_files = []
matched_file_to_dir = {}

if not os.path.exists(stage_dir):
    os.makedirs(stage_dir)

def do_the_thing(to_stage_dir):
    global destinations
    global source_files
    global matched_file_to_dir

    for directory in destination_dirs:
        dirs = [os.path.join(directory, d) for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
        destinations.extend(dirs)

    source_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(source_dir) for f in filenames]

    for sourcefile in source_files:
        for dest in destinations:
            destnames = os.path.basename(dest).split(' ')
            foundit = all(destname.lower() in sourcefile.lower() for destname in destnames)

            if foundit:
                matched_file_to_dir[sourcefile] = dest
                print(f"{os.path.basename(sourcefile)}\n>>\n{dest}\n")
                break

    print()

    if matched_file_to_dir:
        prompt = f"Found {len(matched_file_to_dir)} files{' in staging' if not to_stage_dir else ''}, move to {'staging' if to_stage_dir else 'destinations'}? y to proceed."
        print(prompt)
        resp = input().strip().lower()

        if resp == 'y':
            move_it(to_stage_dir)
    else:
        print("Nothing to move.")

def move_it(to_stage_dir):
    for sourcefile, dest in matched_file_to_dir.items():
        file_to_move = sourcefile
        move_to_dir = stage_dir if to_stage_dir else dest

        shutil.move(file_to_move, move_to_dir)
        print(f"{file_to_move} >> {move_to_dir}")

    if to_stage_dir:
        print("Files moved to staging, run again to move to destinations.")

do_the_thing(not any(os.path.isfile(os.path.join(dp, f)) for dp, dn, filenames in os.walk(stage_dir) for f in filenames))
