---
title: "Implementation"
slug: "sdk-for-flutter-explore-gestures-panlistener-panlistener"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- PanListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../gestures/gestures-library.html">/sdk-for-flutter-explore-gestures-gestures-library</a></li>
<li><a href="../../gestures/PanListener-class.html">/sdk-for-flutter-explore-gestures-panlistener-class</a></li>
<li class="self-crumb">PanListener factory constructor</li>
</ol>
<div class="self-name">PanListener</div>
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
<div class="main-content" data-above-sidebar="gestures/PanListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>PanListener constructor</h1></div>
<section class="multi-line-signature">
PanListener(<wbr/><ol class="parameter-list single-line"> <li>void onPanLambda(<ol class="parameter-list"> <li><a href="../../gestures/GestureState.html">/sdk-for-flutter-explore-gestures-gesturestate</a>, </li>
<li><a href="../../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a>, </li>
<li><a href="../../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a>, </li>
<li>double, </li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Abstract class for handling pan gestures.</p>
<p>Pan gesture occurs when a finger is moving on the screen.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory PanListener(
  void Function(GestureState, Point2D, Point2D, double) onPanLambda,

) =&gt; PanListener$Lambdas(
  onPanLambda,

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
<li><a href="../../gestures/PanListener-class.html">/sdk-for-flutter-explore-gestures-panlistener-class</a></li>
<li class="self-crumb">PanListener factory constructor</li>
</ol>
<h5>PanListener class</h5>
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
