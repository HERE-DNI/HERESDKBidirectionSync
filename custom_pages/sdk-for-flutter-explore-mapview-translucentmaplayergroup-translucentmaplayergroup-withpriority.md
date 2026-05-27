---
title: "TranslucentMapLayerGroup.withPriority constructor"
slug: "sdk-for-flutter-explore-mapview-translucentmaplayergroup-translucentmaplayergroup-withpriority"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TranslucentMapLayerGroup.withPriority.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-translucentmaplayergroup-class</li>
<li class="self-crumb">TranslucentMapLayerGroup.withPriority factory constructor</li>
</ol>
<div class="self-name">TranslucentMapLayerGroup.withPriority</div>
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
<div class="main-content" data-above-sidebar="mapview/TranslucentMapLayerGroup-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>TranslucentMapLayerGroup.withPriority constructor</h1></div>
<section class="multi-line-signature">
TranslucentMapLayerGroup.withPriority(<wbr/><ol class="parameter-list single-line"> <li>String name, </li>
<li>/sdk-for-flutter-explore-mapview-heremapcontrollercore-class aMap, </li>
<li>/sdk-for-flutter-explore-mapview-maplayerpriority-class priority</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates an instance of the group.</p>
<ul>
<li>
<p><code>name</code> Name of the group. Must be unique across /sdk-for-flutter-explore-mapview-maplayer-class and /sdk-for-flutter-explore-mapview-translucentmaplayergroup-class.</p>
</li>
<li>
<p><code>aMap</code> The map to attach the group to.</p>
</li>
<li>
<p><code>priority</code> The /sdk-for-flutter-explore-mapview-maplayerpriority-class which should be applied to position the group.
The /sdk-for-flutter-explore-mapview-maplayerpriority-class must contain only one priority and this priority must have no
category and no group, i.e. /sdk-for-flutter-explore-mapview-maplayerprioritybuilder-ingroup and
/sdk-for-flutter-explore-mapview-maplayerprioritybuilder-withcategory should not be used when building the
/sdk-for-flutter-explore-mapview-maplayerpriority-class.
Example:</p>
</li>
</ul>
<p>new MapLayerPriorityBuilder().renderedAfterLayer("water").build()</p>
<p><code>MapLayerPriorityBuilder().renderedAfterLayer("water").build()</code></p>
<p>Throws /sdk-for-flutter-explore-mapview-translucentmaplayergroupinstantiationexception-class. In case of invalid input parameters.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TranslucentMapLayerGroup.withPriority(String name, HereMapControllerCore aMap, MapLayerPriority priority) =&gt; $prototype.withPriority(name, aMap, priority);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-translucentmaplayergroup-class</li>
<li class="self-crumb">TranslucentMapLayerGroup.withPriority factory constructor</li>
</ol>
<h5>TranslucentMapLayerGroup class</h5>
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
