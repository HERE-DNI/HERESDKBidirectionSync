---
title: "CustomWarningProvider class - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-customwarningprovider-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CustomWarningProvider-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/warner-library-sidebar.html" data-below-sidebar="warner/CustomWarningProvider-class-sidebar.html">

<div>

# <span class="kind-class">CustomWarningProvider</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

A abstract class representing a provider of custom warnings based on vehicle position.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarningprovider-customwarningprovider">CustomWarningProvider</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-getCustomWarningTypeLambda" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">getCustomWarningTypeLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-getWarningsLambda" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-warner-customwarning-class">CustomWarning</a></span>\></span></span> <span class="parameter-name">getWarningsLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a></span>, </span><span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a>?</span></span>)</span>)</span>  
A abstract class representing a provider of custom warnings based on vehicle position.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarningprovider-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarningprovider-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarningprovider-getcustomwarningtype">getCustomWarningType</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ int</span> </span>  
Returns the custom warning type identifier produced by this provider.

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarningprovider-getwarnings">getWarnings</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getWarnings-param-currentSegment" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a></span> <span class="parameter-name">currentSegment</span>, </span><span id="sdk-for-flutter-navigate-getWarnings-param-previousSegment" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a>?</span> <span class="parameter-name">previousSegment</span></span>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-warner-customwarning-class">CustomWarning</a></span>\></span></span> </span>  
Returns a list of custom warnings for the given vehicle position.

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarningprovider-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarningprovider-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-warner-customwarningprovider-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
