var Menu = React.createClass({
    render: function(){
        var menus = ['Home',
                     'About',
                     'Goals',
                     'Contact us']
        return React.createElement('h1', null, menus.map(function(v,i){
            return React.createElement('h1', {key: i},
                                       React.createElement(Link, {label: v})
            )
        })
        )
    }
})
var Link = React.createClass({
    render: function () {
        var url='/' + this.props.label.toLowerCase().trim().replace(' ', '')
        return React.createElement('h1',null, React.createElement(
            'a',
            {href: url},
            this.props.label
        ),React.createElement('br'))
    }
})

ReactDOM.render(
    React.createElement(Menu, null),
    document.getElementById('menu')
)
