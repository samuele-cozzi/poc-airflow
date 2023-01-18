// See https://aka.ms/new-console-template for more information

//string[] args = Environment.GetCommandLineArgs();

if (args.Length > 3) {
    throw new Exception("Errore!!!");
}
else if (args.Length == 0)
{
    Console.WriteLine($"Hello, World!");
}
else{
    foreach (var arg in args){
        Console.WriteLine($"Hello, {arg}!");
    }
}



// using job;
// using Microsoft.Extensions.DependencyInjection;
// using Microsoft.Extensions.Hosting;

// IHost host = Host.CreateDefaultBuilder(args)
//     .ConfigureServices(services =>
//     {
//         services.AddHostedService<Worker>();
//     })
//     .Build();

// await host.RunAsync();