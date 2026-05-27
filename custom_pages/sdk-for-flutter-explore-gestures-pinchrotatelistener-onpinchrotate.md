---
title: "Implementation"
slug: "sdk-for-flutter-explore-gestures-pinchrotatelistener-onpinchrotate"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- onPinchRotate.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../gestures/gestures-library.html">/sdk-for-flutter-explore-gestures-gestures-library</a></li>
<li><a href="../../gestures/PinchRotateListener-class.html">/sdk-for-flutter-explore-gestures-pinchrotatelistener-class</a></li>
<li class="self-crumb">onPinchRotate abstract method</li>
</ol>
<div class="self-name">onPinchRotate</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="gestures/PinchRotateListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>onPinchRotate abstract method</h1></div>
<section class="multi-line-signature">
void
onPinchRotate(<wbr/><ol class="parameter-list"> <li><a href="../../gestures/GestureState.html">/sdk-for-flutter-explore-gestures-gesturestate</a> state, </li>
<li><a href="../../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a> pinchOrigin, </li>
<li><a href="../../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a> rotationOrigin, </li>
<li>double twoFingerDistance, </li>
<li><a href="../../core/Angle-class.html">/sdk-for-flutter-explore-core-angle-class</a> rotation, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Called when the pinch rotate gesture occurs.</p>
<ul>
<li>
<p><code>state</code> Determines in which state the gesture is.</p>
</li>
<li>
<p><code>pinchOrigin</code> Position where the pinch happened relative to the MapView in pixels.</p>
</li>
<li>
<p><code>rotationOrigin</code> Position where the rotation happened relative to the MapView in pixels.</p>
</li>
<li>
<p><code>twoFingerDistance</code> Distance between the two fingers in pixels.</p>
</li>
<li>
<p><code>rotation</code> Fingers rotation angle delta. Indicates how much the fingers rotation angle has changed
since the previous gesture update. Clockwise finger rotation gives positive deltas,
counter clockwise finger rotation gives negative deltas.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onPinchRotate(GestureState state, Point2D pinchOrigin, Point2D rotationOrigin, double twoFingerDistance, Angle rotation);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../gestures/gestures-library.html">/sdk-for-flutter-explore-gestures-gestures-library</a></li>
<li><a href="../../gestures/PinchRotateListener-class.html">/sdk-for-flutter-explore-gestures-pinchrotatelistener-class</a></li>
<li class="self-crumb">onPinchRotate abstract method</li>
</ol>
<h5>PinchRotateListener class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
</HTMLBlock>
