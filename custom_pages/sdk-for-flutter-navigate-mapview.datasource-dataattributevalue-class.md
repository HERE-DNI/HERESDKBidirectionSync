---
title: "DataAttributeValue class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-navigate-mapview.datasource-dataattributevalue-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DataAttributeValue-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/DataAttributeValue-class-sidebar.html">

<div>

# <span class="kind-class">DataAttributeValue</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Encapsulates a data attribute value.

Supports basic types and arrays of basic types.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-dataattributevalue-witharray">DataAttributeValue.withArray</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withArray-param-value" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-class">DataAttributeValue</a></span>\></span></span> <span class="parameter-name">value</span></span>)</span>  
Creates an aggregated data attribute value.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-dataattributevalue-withboolean">DataAttributeValue.withBoolean</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withBoolean-param-value" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">value</span></span>)</span>  
Creates a boolean data attribute value.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-dataattributevalue-withcolor">DataAttributeValue.withColor</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withColor-param-value" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">value</span></span>)</span>  
Creates a color data attribute value.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-dataattributevalue-withdouble">DataAttributeValue.withDouble</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withDouble-param-value" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">value</span></span>)</span>  
Creates a double precision floating decimal data attribute value.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-dataattributevalue-withfloat">DataAttributeValue.withFloat</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withFloat-param-value" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">value</span></span>)</span>  
Creates a single precision floating decimal data attribute value.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-dataattributevalue-withint64">DataAttributeValue.withInt64</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withInt64-param-value" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">value</span></span>)</span>  
Creates a 64-bit integer data attribute value.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-dataattributevalue-withstring">DataAttributeValue.withString</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withString-param-value" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">value</span></span>)</span>  
Creates a string data attribute value.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-getarray">getArray</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-class">DataAttributeValue</a></span>\></span>?</span> </span>  
Gets the array value or `null` if the type doesn't match.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-getasstring">getAsString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
Returns a string representation of the contained value.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-getboolean">getBoolean</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ bool?</span> </span>  
Gets the boolean value or `null` if the type doesn't match.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-getcolor">getColor</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ Color?</span> </span>  
Gets the color value or `null` if the type doesn't match.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-getdouble">getDouble</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ double?</span> </span>  
Gets the double precision floating decimal value or `null` if the type doesn't match.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-getfloat">getFloat</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ double?</span> </span>  
Gets the single precision floating decimal value or `null` if the type doesn't match.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-getint64">getInt64</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ int?</span> </span>  
Gets 64-bits integer value or `null` if the type doesn't match.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-getstring">getString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String?</span> </span>  
Gets the string value or `null` if the type doesn't match.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-gettype">getType</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevaluevaluetype">DataAttributeValueValueType</a></span> </span>  
Returns the type of the value.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
