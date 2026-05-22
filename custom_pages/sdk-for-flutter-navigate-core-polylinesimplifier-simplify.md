---
title: "Untitled"
slug: "sdk-for-flutter-navigate-core-polylinesimplifier-simplify"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- simplify.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li>/sdk-for-flutter-navigate-core-polylinesimplifier-class</li>
<li class="self-crumb">simplify abstract method</li>
</ol>
<div class="self-name">simplify</div>
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
<div class="main-content" data-above-sidebar="core/PolylineSimplifier-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>simplify abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-threading-taskhandle-class
simplify(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class&gt; polyline, </li>
<li>/sdk-for-flutter-navigate-core-polylinesimplifieroptions-class simplificationParameters, </li>
<li>/sdk-for-flutter-navigate-core-polylinesimplificationcallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Reduces the number of points in the input polyline.</p>
<p>Does this by removing points which are not significant
according to the passed /sdk-for-flutter-navigate-core-polylinesimplifieroptions-class.
Simplification process is performed on the device without
connecting to the network and is computationally intensive.</p>
<ul>
<li>
<p><code>polyline</code> Input polyline that should be reduced in size.</p>
</li>
<li>
<p><code>simplificationParameters</code> Strategy, that controls the behavior of the underlying algorithm.</p>
</li>
<li>
<p><code>callback</code> Callback, which will be invoked on the main thread,
when operation is finished.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-core-threading-taskhandle-class. Controls an asynchronous operation.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle simplify(List&lt;GeoCoordinates&gt; polyline, PolylineSimplifierOptions simplificationParameters, PolylineSimplificationCallback callback);</code></pre>
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
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li>/sdk-for-flutter-navigate-core-polylinesimplifier-class</li>
<li class="self-crumb">simplify abstract method</li>
</ol>
<h5>PolylineSimplifier class</h5>
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
