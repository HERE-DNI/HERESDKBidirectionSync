---
title: "Implementation"
slug: "sdk-for-flutter-explore-gestures-longpresslistener-longpresslistener"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- LongPressListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../gestures/gestures-library.html">/sdk-for-flutter-explore-gestures-gestures-library</a></li>
<li><a href="../../gestures/LongPressListener-class.html">/sdk-for-flutter-explore-gestures-longpresslistener-class</a></li>
<li class="self-crumb">LongPressListener factory constructor</li>
</ol>
<div class="self-name">LongPressListener</div>
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
<div class="main-content" data-above-sidebar="gestures/LongPressListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>LongPressListener constructor</h1></div>
<section class="multi-line-signature">
LongPressListener(<wbr/><ol class="parameter-list single-line"> <li>void onLongPressLambda(<ol class="parameter-list single-line"> <li><a href="../../gestures/GestureState.html">/sdk-for-flutter-explore-gestures-gesturestate</a>, </li>
<li><a href="../../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a></li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Abstract class for handling long-press gestures.</p>
<p>Long-press gesture occurs after tapping and holding the finger for a long time on the screen.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory LongPressListener(
  void Function(GestureState, Point2D) onLongPressLambda,

) =&gt; LongPressListener$Lambdas(
  onLongPressLambda,

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
<li><a href="../../gestures/LongPressListener-class.html">/sdk-for-flutter-explore-gestures-longpresslistener-class</a></li>
<li class="self-crumb">LongPressListener factory constructor</li>
</ol>
<h5>LongPressListener class</h5>
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
