use std::env;
use std::path::Path;
use std::collections::HashMap;
use std::fs::File;
use std::io::prelude::*;

fn main() {
    let args: Vec<String> = env::args().collect();

    // check we have 1 argument
    if args.len() != 2 {
        let path = Path::new(&args[0]);
        let file = path.file_name().expect("Couldn't get filename");
        println!("  Usage: {:?} DNA", file);
        ::std::process::exit(1);
    }

    let input = &args[1];
    let mut hash = HashMap::new();

    // initialize
    //let bases = vec!['A', 'C', 'G', 'T'];
    let bases = String::from("ACGT");
    //for base in &bases {
    for base in bases.chars() {
        hash.insert(base, 0);
    }
    
    // figure out if the input is from a string or a file
    let path = Path::new(input);
    let mut dna = String::new();
    match path.is_file() {
        true => {
            let mut file = File::open(path).expect("Can't open input");
            file.read_to_string(&mut dna).expect("Can't read input");
        },
        false => {
            dna = input.clone();
        }
    }

    // count
    for letter in dna.to_uppercase().chars() {
        let counter = hash.entry(letter).or_insert(0);
        *counter += 1;
    }

    //println!("{} {} {} {}", hash[&'A'], hash[&'C'], hash[&'G'], hash[&'T']);
    let counts : Vec<u32> = bases.chars().map(|b| hash[&b]).collect();
    println!("{:?}", counts);
    //println!("{} {} {} {}", hash[&'A'], hash[&'C'], hash[&'G'], hash[&'T']);
    println!(counts.join(" "));
}
