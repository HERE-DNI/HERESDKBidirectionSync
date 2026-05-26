---
title: "renderedAfterLayerWithCategory abstract method"
slug: "sdk-for-flutter-explore-mapview-maplayerprioritybuilder-renderedafterlayerwithcategory"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- renderedAfterLayerWithCategory.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-maplayerprioritybuilder-class</li>
<li class="self-crumb">renderedAfterLayerWithCategory abstract method</li>
</ol>
<div class="self-name">renderedAfterLayerWithCategory</div>
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
<h1>renderedAfterLayerWithCategory abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-mapview-maplayerprioritybuilder-class
renderedAfterLayerWithCategory(<wbr/><ol class="parameter-list single-line"> <li>String referenceLayer, </li>
<li>String referenceCategory</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets the priority as rendered after the referenceCategory of the referenceLayer.</p>
<p>Applies to the
layer itself or the category pointed to by the preceding call to
/sdk-for-flutter-explore-mapview-maplayerprioritybuilder-withcategory.
Notice that the order of calls to the functions
<code>renderedFirst|Last|Before|After</code>
matters, and that after such a call the builder clears the current category and refers again to
the layer itself. Further, only one priority for each layer and layer category should be set
with these functions since previous priorities would be ingored. For example the priority to
render layer category 'C' after layer 'L' would be overridden by the priority to
render layer category 'C' before layer 'L' when building something like</p>
<p><code>withCategory("C").renderedAfterLayer("L").withCategory("C").renderedBeforeLayer("L")</code></p>
<p>The previously defined and prioritised categories can be used as reference.
If the referenceLayer and/or the referenceCategory do not exist, then the function will set
the priority as rendered after all layers and categories.</p>
<ul>
<li>
<p><code>referenceLayer</code> The beforehand defined layer name which renders directly before the current layer.</p>
</li>
<li>
<p><code>referenceCategory</code> The beforehand defined category name which renders directly before the current layer.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-explore-mapview-maplayerprioritybuilder-class. This class instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapLayerPriorityBuilder renderedAfterLayerWithCategory(String referenceLayer, String referenceCategory);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-maplayerprioritybuilder-class</li>
<li class="self-crumb">renderedAfterLayerWithCategory abstract method</li>
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
