---
title: "HereMap class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-heremap-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- HereMap-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/HereMap-class-sidebar.html">

<div>

# <span class="kind-class">HereMap</span> class

</div>

<div class="section desc markdown">

Widget that displays a map. To interact with the map, use the <a href="sdk-for-flutter-explore-mapview-heremapcontroller-class">HereMapController</a> object that is passed to <a href="sdk-for-flutter-explore-mapview-heremapcreatedcallback">HereMapCreatedCallback</a> Note: Before using this class, <a href="sdk-for-flutter-explore-core-engine-sdknativeengine-class">SDKNativeEngine</a> must be already initialized.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremap-heremap">HereMap</a></span><span class="signature">({<span id="sdk-for-flutter-explore-param-key" class="parameter"><span class="type-annotation">Key?</span> <span class="parameter-name">key</span>, </span><span id="sdk-for-flutter-explore-param-onMapCreated" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-heremapcreatedcallback">HereMapCreatedCallback</a>?</span> <span class="parameter-name">onMapCreated</span>, </span><span id="sdk-for-flutter-explore-param-gestureRecognizers" class="parameter"><span class="type-annotation">Set<span class="signature">\<<wbr></wbr><span class="type-parameter">Factory<span class="signature">\<<wbr></wbr><span class="type-parameter">OneSequenceGestureRecognizer</span>\></span></span>\></span>?</span> <span class="parameter-name">gestureRecognizers</span>, </span><span id="sdk-for-flutter-explore-param-mode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-nativeviewmode">NativeViewMode</a></span> <span class="parameter-name">mode</span> = <span class="default-value">NativeViewMode.virtualDisplay</span>, </span><span id="sdk-for-flutter-explore-param-options" class="parameter"><span class="type-annotation">dynamic</span> <span class="parameter-name">options</span></span>})</span>  
Creates a widget that displays a map.

<div class="constructor-modifier features">

const

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremap-gesturerecognizers">gestureRecognizers</a></span> <span class="signature">→ Set<span class="signature">\<<wbr></wbr><span class="type-parameter">Factory<span class="signature">\<<wbr></wbr><span class="type-parameter">OneSequenceGestureRecognizer</span>\></span></span>\></span>?</span>  
Which gestures should be consumed by the map.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremap-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremap-key">key</a></span> <span class="signature">→ Key?</span>  
Controls how one widget replaces another widget in the tree.

<div class="features">

<span class="feature">final</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremap-mode">mode</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-mapview-nativeviewmode">NativeViewMode</a></span>  
Which method of hosting Android native view (the map) will be used. Default value is <a href="sdk-for-flutter-explore-mapview-nativeviewmode">NativeViewMode.virtualDisplay</a>.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremap-onmapcreated">onMapCreated</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-mapview-heremapcreatedcallback">HereMapCreatedCallback</a>?</span>  
Method called when the map is ready to be used.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremap-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremap-createelement">createElement</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ StatefulElement</span> </span>  
Creates a `StatefulElement` to manage this widget's location in the tree.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremap-createstate">createState</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ State<span class="signature">\<<wbr></wbr><span class="type-parameter">StatefulWidget</span>\></span></span> </span>  
Creates the mutable state for this widget at a given location in the tree.

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremap-debugdescribechildren">debugDescribeChildren</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter">DiagnosticsNode</span>\></span></span> </span>  
Returns a list of `DiagnosticsNode` objects describing this node's children.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremap-debugfillproperties">debugFillProperties</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-debugFillProperties-param-properties" class="parameter"><span class="type-annotation">DiagnosticPropertiesBuilder</span> <span class="parameter-name">properties</span></span>) <span class="returntype parameter">→ void</span> </span>  
Add additional properties associated with the node.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremap-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremap-todiagnosticsnode">toDiagnosticsNode</a></span><span class="signature">(<wbr></wbr>{<span id="sdk-for-flutter-explore-toDiagnosticsNode-param-name" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">name</span>, </span><span id="sdk-for-flutter-explore-toDiagnosticsNode-param-style" class="parameter"><span class="type-annotation">DiagnosticsTreeStyle?</span> <span class="parameter-name">style</span></span>}) <span class="returntype parameter">→ DiagnosticsNode</span> </span>  
Returns a debug representation of the object that is used by debugging tools and by `DiagnosticsNode.toStringDeep`.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremap-tostring">toString</a></span><span class="signature">(<wbr></wbr>{<span id="sdk-for-flutter-explore-toString-param-minLevel" class="parameter"><span class="type-annotation">DiagnosticLevel</span> <span class="parameter-name">minLevel</span> = <span class="default-value">DiagnosticLevel.info</span></span>}) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremap-tostringdeep">toStringDeep</a></span><span class="signature">(<wbr></wbr>{<span id="sdk-for-flutter-explore-toStringDeep-param-prefixLineOne" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">prefixLineOne</span> = <span class="default-value">''</span>, </span><span id="sdk-for-flutter-explore-toStringDeep-param-prefixOtherLines" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">prefixOtherLines</span>, </span><span id="sdk-for-flutter-explore-toStringDeep-param-minLevel" class="parameter"><span class="type-annotation">DiagnosticLevel</span> <span class="parameter-name">minLevel</span> = <span class="default-value">DiagnosticLevel.debug</span>, </span><span id="sdk-for-flutter-explore-toStringDeep-param-wrapWidth" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">wrapWidth</span> = <span class="default-value">65</span></span>}) <span class="returntype parameter">→ String</span> </span>  
Returns a string representation of this node and its descendants.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremap-tostringshallow">toStringShallow</a></span><span class="signature">(<wbr></wbr>{<span id="sdk-for-flutter-explore-toStringShallow-param-joiner" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">joiner</span> = <span class="default-value">', '</span>, </span><span id="sdk-for-flutter-explore-toStringShallow-param-minLevel" class="parameter"><span class="type-annotation">DiagnosticLevel</span> <span class="parameter-name">minLevel</span> = <span class="default-value">DiagnosticLevel.debug</span></span>}) <span class="returntype parameter">→ String</span> </span>  
Returns a one-line detailed description of the object.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremap-tostringshort">toStringShort</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A short, textual description of this widget.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremap-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
