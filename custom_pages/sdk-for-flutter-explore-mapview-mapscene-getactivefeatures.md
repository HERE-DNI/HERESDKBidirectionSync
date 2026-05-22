---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mapscene-getactivefeatures"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getActiveFeatures.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapscene-class</li>
<li class="self-crumb">getActiveFeatures abstract method</li>
</ol>
<div class="self-name">getActiveFeatures</div>
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
<div class="main-content" data-above-sidebar="mapview/MapScene-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>getActiveFeatures abstract method</h1></div>
<section class="multi-line-signature">
Map&lt;<wbr/>String, String&gt;
getActiveFeatures(<wbr/>)

      

    </section>
<section class="desc markdown">
<p>Gets map features that are currently active.</p>
<p>Active features are features that are either
enabled via a call to /sdk-for-flutter-explore-mapview-mapscene-enablefeatures or that are enabled by default in the scene.</p>
<p>The key to the resulting map is the name of the feature
and the value is the active mode.</p>
<p>Result is empty if scene has not been loaded.</p>
<p>Returns <code>Map&lt;String, String&gt;</code>. The map of active features.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Map&lt;String, String&gt; getActiveFeatures();</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapscene-class</li>
<li class="self-crumb">getActiveFeatures abstract method</li>
</ol>
<h5>MapScene class</h5>
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
