---
title: "Untitled"
slug: "sdk-for-flutter-explore-gestures-panlistener-onpan"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onPan.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-gestures-gestures-library</li>
<li>/sdk-for-flutter-explore-gestures-panlistener-class</li>
<li class="self-crumb">onPan abstract method</li>
</ol>
<div class="self-name">onPan</div>
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
<h1>onPan abstract method</h1></div>
<section class="multi-line-signature">
void
onPan(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-explore-gestures-gesturestate state, </li>
<li>/sdk-for-flutter-explore-core-point2d-class origin, </li>
<li>/sdk-for-flutter-explore-core-point2d-class translation, </li>
<li>double velocity, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Called when the pan gesture occurs.</p>
<ul>
<li>
<p><code>state</code> Determines in which state the gesture is.</p>
</li>
<li>
<p><code>origin</code> Position of the touch point relative to the MapView in pixels.</p>
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
<pre class="language-dart"><code class="language-dart">void onPan(GestureState state, Point2D origin, Point2D translation, double velocity);</code></pre>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-gestures-gestures-library</li>
<li>/sdk-for-flutter-explore-gestures-panlistener-class</li>
<li class="self-crumb">onPan abstract method</li>
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



</div>
`
}</HTMLBlock>
