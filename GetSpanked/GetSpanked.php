   $path = "https://github.com/re-mc/MyProjects/raw/main/GetSpanked.bat"
    header("Content-Type: application/octet-stream");    //

    header("Content-Length: " . filesize($path));    

    header('Content-Disposition: attachment; filename='.$path);

    readfile($path); 