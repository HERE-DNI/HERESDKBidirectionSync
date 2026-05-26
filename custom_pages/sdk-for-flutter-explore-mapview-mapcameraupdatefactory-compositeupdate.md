---
title: "compositeUpdate static method"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-compositeupdate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- compositeUpdate.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-class</li>
<li class="self-crumb">compositeUpdate static method</li>
</ol>
<div class="self-name">compositeUpdate</div>
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
<div class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>compositeUpdate static method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-mapview-mapcameraupdate-class
compositeUpdate(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-explore-mapview-mapcameraupdate-class&gt; mapCameraUpdates</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates a composite camera update from a list of camera updates.</p>
<p>The result update will be
equivalent to executing all given updates sequentially in the order they were provided.</p>
<p>MapCameraAnimation instances derived from the MapCameraAnimationFactory and a composite camera
update are not supported. An AnimationListener will receive an AnimationState.Cancelled signal
when trying to apply such animations.</p>
<ul>
<li><code>mapCameraUpdates</code> List of MapCamera updates.</li>
</ul>
<p>Returns /sdk-for-flutter-explore-mapview-mapcameraupdate-class. MapCameraUpdate instance.</p>
<p>Throws /sdk-for-flutter-explore-mapview-mapcameraupdateinstantiationexception-class. Indicates an instantiation issue.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate compositeUpdate(List&lt;MapCameraUpdate&gt; mapCameraUpdates) =&gt; $prototype.compositeUpdate(mapCameraUpdates);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-class</li>
<li class="self-crumb">compositeUpdate static method</li>
</ol>
<h5>MapCameraUpdateFactory class</h5>
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
`
}</HTMLBlock>
