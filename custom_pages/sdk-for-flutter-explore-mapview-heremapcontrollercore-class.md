---
title: "HereMapControllerCore class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-heremapcontrollercore-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- HereMapControllerCore-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/HereMapControllerCore-class-sidebar.html">

<div>

# <span class="kind-class">HereMapControllerCore</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

The representation of a dynamic and interactive geographic map.

The map manages a collection of layers of objects and spaces, presents them in a stacked layout and offers the means to focus on a certain area. The layers, their relation to the objects and spaces, the layout and the representation style is described through a configuration.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-heremapcontrollercore">HereMapControllerCore</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-style">style</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-mapview-style-class">Style</a></span>  
The style that the map uses to customize the visual appearance of rendered features. Changes made to the map style using <a href="sdk-for-flutter-explore-mapview-style-update">Style.update</a> are lost when new scene is loaded using <a href="sdk-for-flutter-explore-mapview-mapscene-loadsceneformapscheme">MapScene.loadSceneForMapScheme</a> and its variants as well as when map features are enabled or disabled using <a href="sdk-for-flutter-explore-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a> and <a href="sdk-for-flutter-explore-mapview-mapscene-disablefeatures">MapScene.disableFeatures</a>.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-addmapidlelistener">addMapIdleListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-addMapIdleListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapidlelistener-class">MapIdleListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a listener for receiving idle state notifications and notifies it of the current state.

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-removemapidlelistener">removeMapIdleListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-removeMapIdleListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapidlelistener-class">MapIdleListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a listener from receiving idle state notifications.

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
