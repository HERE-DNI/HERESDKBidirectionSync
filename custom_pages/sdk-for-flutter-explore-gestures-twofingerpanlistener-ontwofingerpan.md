---
title: "Implementation"
slug: "sdk-for-flutter-explore-gestures-twofingerpanlistener-ontwofingerpan"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- onTwoFingerPan.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../gestures/gestures-library.html">/sdk-for-flutter-explore-gestures-gestures-library</a></li>
<li><a href="../../gestures/TwoFingerPanListener-class.html">/sdk-for-flutter-explore-gestures-twofingerpanlistener-class</a></li>
<li class="self-crumb">onTwoFingerPan abstract method</li>
</ol>
<div class="self-name">onTwoFingerPan</div>
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
<div class="main-content" data-above-sidebar="gestures/TwoFingerPanListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>onTwoFingerPan abstract method</h1></div>
<section class="multi-line-signature">
void
onTwoFingerPan(<wbr/><ol class="parameter-list"> <li><a href="../../gestures/GestureState.html">/sdk-for-flutter-explore-gestures-gesturestate</a> state, </li>
<li><a href="../../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a> origin, </li>
<li><a href="../../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a> translation, </li>
<li>double velocity, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Called when the two finger pan gesture occurs.</p>
<ul>
<li>
<p><code>state</code> Determines in which state the gesture is.</p>
</li>
<li>
<p><code>origin</code> Position halfway between two touch points relative to the MapView in pixels.</p>
</li>
<li>
<p><code>translation</code> Translation offset since the last position in pixels.</p>
</li>
<li>
<p><code>velocity</code> Velocity of panning in pixels per millisecond.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onTwoFingerPan(GestureState state, Point2D origin, Point2D translation, double velocity);</code></pre>
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
<li><a href="../../gestures/TwoFingerPanListener-class.html">/sdk-for-flutter-explore-gestures-twofingerpanlistener-class</a></li>
<li class="self-crumb">onTwoFingerPan abstract method</li>
</ol>
<h5>TwoFingerPanListener class</h5>
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
