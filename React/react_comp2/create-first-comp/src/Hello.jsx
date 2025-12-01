function Hello(){
    let myname = "Kashish";
    let fullName = () => {
        return "Kashish Soni";
    }
    return <h3>
        Hello from Hello Component {fullName ()};
    </h3>
}

export default Hello;