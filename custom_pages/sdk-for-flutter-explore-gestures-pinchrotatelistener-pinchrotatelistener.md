---
title: "Implementation"
slug: "sdk-for-flutter-explore-gestures-pinchrotatelistener-pinchrotatelistener"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- PinchRotateListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../gestures/gestures-library.html">/sdk-for-flutter-explore-gestures-gestures-library</a></li>
<li><a href="../../gestures/PinchRotateListener-class.html">/sdk-for-flutter-explore-gestures-pinchrotatelistener-class</a></li>
<li class="self-crumb">PinchRotateListener factory constructor</li>
</ol>
<div class="self-name">PinchRotateListener</div>
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
<h1>PinchRotateListener constructor</h1></div>
<section class="multi-line-signature">
PinchRotateListener(<wbr/><ol class="parameter-list single-line"> <li>void onPinchRotateLambda(<ol class="parameter-list"> <li><a href="../../gestures/GestureState.html">/sdk-for-flutter-explore-gestures-gesturestate</a>, </li>
<li><a href="../../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a>, </li>
<li><a href="../../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a>, </li>
<li>double, </li>
<li><a href="../../core/Angle-class.html">/sdk-for-flutter-explore-core-angle-class</a>, </li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Abstract class for handling pinch rotate gestures.</p>
<p>Pinch rotate gesture occurs when two fingers are on the screen
and at least one of them moves.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory PinchRotateListener(
  void Function(GestureState, Point2D, Point2D, double, Angle) onPinchRotateLambda,

) =&gt; PinchRotateListener$Lambdas(
  onPinchRotateLambda,

);</code></pre>
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
<li class="self-crumb">PinchRotateListener factory constructor</li>
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
