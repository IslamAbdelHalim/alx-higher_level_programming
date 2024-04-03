How to select HTML elements in JavaScript?
by document.querySelector(element);

How to select HTML elements with JQuery?
$(selector)

What are differences between ID, class and tag name selectors?
id => is uniqe and can not two element has the same id 

class => can be repeate where more than element can have the same class to share the same features

tag name => is a tag name that element

How to modify an HTML element style?
element.style.property = "value";
or element.style.setProperty(property name, "value");
or element.style.removeProperty(propertyName);

or if you want modify inside css files
document.stylesheet[index'if have more than one css file'].rules[index of element].style.remove or setProperty();

how modify the Dom?
by prepend() or append()
