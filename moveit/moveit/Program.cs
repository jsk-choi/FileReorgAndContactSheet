using System.Linq;

string[] destinationDirs = new string[] { "Q:\\00", "Q:\\00\\_ tg" };
string sourceDir = "Q:\\zz-org";
string stageDir = "Q:\\00\\__from__";



List<DirectoryInfo> destinations = new();
List<FileInfo> sourceFiles = new();
Dictionary<FileInfo, DirectoryInfo> matchedFileToDir = new();














if (!Directory.Exists(stageDir))
{
    Directory.CreateDirectory(stageDir);
}

DoTheThing(
    !Directory.GetFiles(stageDir, "*.*", SearchOption.AllDirectories).Any()
);


void DoTheThing(bool toStageDir)
{

    foreach (string directory in destinationDirs)
    {
        var dirs = Directory.GetDirectories(directory).Select(x => new DirectoryInfo(x));
        destinations.AddRange(dirs);
    }

    sourceFiles = Directory.GetFiles(sourceDir, "*.*", SearchOption.AllDirectories).Select(x => new FileInfo(x)).ToList();

    foreach (var sourcefile in sourceFiles)
    {

        foreach (var dest in destinations)
        {
            string[] destnames = dest.Name.Split(' ');
            bool foundit = destnames.All(dest => sourcefile.FullName.Contains(dest, StringComparison.OrdinalIgnoreCase));

            if (foundit)
            {
                var nl = Environment.NewLine;
                matchedFileToDir.Add(sourcefile, dest);
                Console.WriteLine($"{sourcefile.Name}{nl}>>{nl}{dest.FullName}{nl}{nl}");
                break;
            }
        }
    }

    Console.WriteLine();

    if (matchedFileToDir.Any())
    {
        string prompt = $"Found {matchedFileToDir.Count} files{(toStageDir ? "" : " in staging")}, move to {(toStageDir ? " staging" : " destinations")}? y to proceed.";
        Console.WriteLine(prompt);
        string resp = Console.ReadLine()!;

        if (resp.ToLower().Trim() == "y")
        {
            MoveIt(toStageDir);
        }

    }
    else
    {
        Console.WriteLine("Nothing to move.");
    }


}

void MoveIt(bool toStageDir)
{

    foreach (var movefile in matchedFileToDir)
    {
        string filetomove = movefile.Key.FullName;
        string movetodir = toStageDir ? stageDir : movefile.Value.FullName;

        File.Move(filetomove, movetodir);
        Console.WriteLine($"{filetomove} >> {movetodir}");
    }

    if (toStageDir)
    {
        Console.WriteLine("Files move to staging, run again to move to destinations.");
    }

}