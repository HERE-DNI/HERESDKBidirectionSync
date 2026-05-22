---
title: "Untitled"
slug: "sdk-for-flutter-navigate-gestures-pinchrotatelistener-pinchrotatelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PinchRotateListener.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-gestures-gestures-library</li>
<li>/sdk-for-flutter-navigate-gestures-pinchrotatelistener-class</li>
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
PinchRotateListener(<wbr/><ol class="parameter-list single-line"> <li>void onPinchRotateLambda(<ol class="parameter-list"> <li>/sdk-for-flutter-navigate-gestures-gesturestate, </li>
<li>/sdk-for-flutter-navigate-core-point2d-class, </li>
<li>/sdk-for-flutter-navigate-core-point2d-class, </li>
<li>double, </li>
<li>/sdk-for-flutter-navigate-core-angle-class, </li>
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-gestures-gestures-library</li>
<li>/sdk-for-flutter-navigate-gestures-pinchrotatelistener-class</li>
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



</div>
`
}</HTMLBlock>
