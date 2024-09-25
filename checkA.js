

function main() {
    let word = "ssdfds"
    let lilWord = word.toLowerCase()
    let hasA = lilWord.includes('a');
    if (!hasA) {
        console.log("Não contém a's")
        return
    }
    let count = lilWord.split('a').length - 1;
    console.log(`A letra a aparece ${count} vezes`)
}

main()