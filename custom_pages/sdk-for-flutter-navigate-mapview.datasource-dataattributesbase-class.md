---
title: "DataAttributesBase class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-navigate-mapview.datasource-dataattributesbase-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/DataAttributesBase-class-sidebar.html">

<div>

# <span class="kind-class">DataAttributesBase</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Interface for a collection of data attributes.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section">

Implementers  
- <a href="sdk-for-flutter-navigate-mapview-datasource-dataattributes-class">DataAttributes</a>
- <a href="sdk-for-flutter-navigate-mapview-datasource-dataattributesaccessor-class">DataAttributesAccessor</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-dataattributesbase">DataAttributesBase</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-getAttributeNamesLambda" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">getAttributeNamesLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-getValueTypeLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevaluevaluetype">DataAttributeValueValueType</a>?</span> <span class="parameter-name">getValueTypeLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">String</span></span>), </span><span id="sdk-for-flutter-navigate-param-getAsStringLambda" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">getAsStringLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">String</span></span>), </span><span id="sdk-for-flutter-navigate-param-getStringLambda" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">getStringLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">String</span></span>), </span><span id="sdk-for-flutter-navigate-param-getInt64Lambda" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">getInt64Lambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">String</span></span>), </span><span id="sdk-for-flutter-navigate-param-getFloatLambda" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">getFloatLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">String</span></span>), </span><span id="sdk-for-flutter-navigate-param-getDoubleLambda" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">getDoubleLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">String</span></span>), </span><span id="sdk-for-flutter-navigate-param-getBooleanLambda" class="parameter"><span class="type-annotation">bool?</span> <span class="parameter-name">getBooleanLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">String</span></span>), </span><span id="sdk-for-flutter-navigate-param-getValueLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-class">DataAttributeValue</a>?</span> <span class="parameter-name">getValueLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">String</span></span>)</span>)</span>  
Interface for a collection of data attributes.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-getasstring">getAsString</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getAsString-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span></span>) <span class="returntype parameter">→ String?</span> </span>  
Gets the value of an attribute as a string or `null` if it is not contained.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-getattributenames">getAttributeNames</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> </span>  
Returns a list of attribute names.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-getboolean">getBoolean</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getBoolean-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span></span>) <span class="returntype parameter">→ bool?</span> </span>  
Gets the value of a boolean attribute or `null` if it is not contained or the type doesn't match.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-getdouble">getDouble</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getDouble-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span></span>) <span class="returntype parameter">→ double?</span> </span>  
Gets the value of a double precision floating decimal attribute or `null` if it is not contained or the type doesn't match.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-getfloat">getFloat</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getFloat-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span></span>) <span class="returntype parameter">→ double?</span> </span>  
Gets the value of a single precision floating decimal attribute or `null` if it is not contained or the type doesn't match.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-getint64">getInt64</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getInt64-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span></span>) <span class="returntype parameter">→ int?</span> </span>  
Gets the value of a 64-bits integer attribute or `null` if it is not contained or the type doesn't match.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-getstring">getString</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getString-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span></span>) <span class="returntype parameter">→ String?</span> </span>  
Gets the value of a string attribute or `null` if it is not contained or the type doesn't match.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-getvalue">getValue</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getValue-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-class">DataAttributeValue</a>?</span> </span>  
Gets the DataAttributeValue or `null` if it is not contained.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-getvaluetype">getValueType</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getValueType-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-datasource-dataattributevaluevaluetype">DataAttributeValueValueType</a>?</span> </span>  
Returns the value type of an attribute or `null` if it is not contained.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

