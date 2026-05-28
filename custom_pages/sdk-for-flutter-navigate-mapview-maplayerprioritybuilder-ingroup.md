---
title: "inGroup abstract method"
slug: "sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-ingroup"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- inGroup.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class</li>
<li class="self-crumb">inGroup abstract method</li>
</ol>
<div class="self-name">inGroup</div>
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
<div class="main-content" data-above-sidebar="mapview/MapLayerPriorityBuilder-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>inGroup abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class
inGroup(<wbr/><ol class="parameter-list single-line"> <li>String group</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets the group for which a priority could be defined with the next call to the functions
<code>renderedFirst|Last|BeforeLayer|AfterLayer</code>.</p>
<p>When a group is set, the next defined priority is relative to the layers and layer categories
inside this group. The references (i.e. 'referenceLayer' and 'referenceCategory') of the priority
are only searched inside the group.
Only one group or no group can be defined per layer priority and layer category priority, however,
different layers can set priorities for the same group.
After a priority is defined by calling one of the aforementioned functions, the current group
is cleared and the builder refers again to the global layer list in the scene.
Note that a group needs to exist when the built /sdk-for-flutter-navigate-mapview-maplayerpriority-class is used during a
/sdk-for-flutter-navigate-mapview-maplayerbuilder-build or /sdk-for-flutter-navigate-mapview-maplayer-setpriority, otherwise the priority
cannot be applied and the layer will render nothing to the group.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li><code>group</code> The name of the group. For instance the name of a /sdk-for-flutter-navigate-mapview-translucentmaplayergroup-class.</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class. This class instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapLayerPriorityBuilder inGroup(String group);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class</li>
<li class="self-crumb">inGroup abstract method</li>
</ol>
<h5>MapLayerPriorityBuilder class</h5>
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
