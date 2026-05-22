---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-avoidanceoptions-segments"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- segments.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-avoidanceoptions-class</li>
<li class="self-crumb">segments property</li>
</ol>
<div class="self-name">segments</div>
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
<div class="main-content" data-above-sidebar="routing/AvoidanceOptions-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>segments property</h1></div>
<section class="multi-line-signature">
        
        List&lt;<wbr/>/sdk-for-flutter-navigate-routing-segmentreference-class&gt;
segments
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Segments that routes will avoid going through.
Violations are reported as /sdk-for-flutter-navigate-routing-sectionnoticecode.</p>
<p><strong>Notes:</strong></p>
<ul>
<li>This avoidance option is not supported in <code>IsolineOptions</code> for isoline calculation.</li>
<li>The engine does not support an unlimited number of segments to avoid.
The limit is defined by the HERE backend services and may change. For now,
the maximum number of segments to avoid should be below 250. This value may change
on the backend and it is therefore not guaranteed to be stable.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;SegmentReference&gt; segments;</code></pre>
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
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-avoidanceoptions-class</li>
<li class="self-crumb">segments property</li>
</ol>
<h5>AvoidanceOptions class</h5>
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
