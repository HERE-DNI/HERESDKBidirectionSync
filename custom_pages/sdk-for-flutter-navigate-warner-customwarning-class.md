---
title: "CustomWarning class - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-customwarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CustomWarning-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/warner-library-sidebar.html" data-below-sidebar="warner/CustomWarning-class-sidebar.html">

<div>

# <span class="kind-class">CustomWarning</span> class

</div>

<div class="section desc markdown">

class container for custom warning data.

This structure represents the type-specific payload associated with a custom warning.

Instances of this structure are typically produced by custom warning evaluation logic and may also be retrieved from the `WarningRegistry`.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarning-customwarning">CustomWarning</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarning-customwarningtype">customWarningType</a></span> <span class="signature">↔ int</span>  
Identifier of the custom warning type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarning-endoffsetinmeters">endOffsetInMeters</a></span> <span class="signature">↔ double?</span>  
End offset of the warning range along the segment.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarning-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarning-id">id</a></span> <span class="signature">↔ int</span>  
Identifier of the warning. The ID is unique only within its specific <a href="sdk-for-flutter-navigate-warner-customwarning-customwarningtype">CustomWarning.customWarningType</a> and can be used to retrieve additional information from a corresponding registry.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarning-payload">payload</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-metadata-class">Metadata</a>?</span>  
Custom warning payload.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarning-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarning-startoffsetinmeters">startOffsetInMeters</a></span> <span class="signature">↔ double</span>  
Start offset of the warning range along the segment.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarning-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarning-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarning-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
