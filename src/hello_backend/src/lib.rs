#[ic_cdk::query]
fn greet(name: String) -> String {
    if name.is_empty() {
        "This is".to_string()
    } else {
        format!("This [{name}] here is")
    }
}
