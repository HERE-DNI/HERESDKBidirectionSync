---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-maplayerprioritybuilder-renderedlast"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- renderedLast.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-maplayerprioritybuilder-class</li>
<li class="self-crumb">renderedLast abstract method</li>
</ol>
<div class="self-name">renderedLast</div>
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
<h1>renderedLast abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-mapview-maplayerprioritybuilder-class
renderedLast(<wbr/>)

      

    </section>
<section class="desc markdown">
<p>Sets the priority as rendered after all layers and categories.</p>
<p>Applies to the layer itself or the
category pointed to by the preceding call to /sdk-for-flutter-explore-mapview-maplayerprioritybuilder-withcategory.
Notice that the order of calls to the functions
<code>renderedFirst|Last|Before|After</code>
matters, and that after such a call the builder clears the current category and refers again to
the layer itself. Further, only one priority for each layer and layer category should be set
with these functions since previous priorities would be ingored. For example the priority to
render layer category 'C' after layer 'L' would be overridden by the priority to
render layer category 'C' before layer 'L' when building something like</p>
<p><code>withCategory("C").renderedAfterLayer("L").withCategory("C").renderedBeforeLayer("L")</code></p>
<p>The previously defined and prioritised categories can be used as reference.</p>
<p>Returns /sdk-for-flutter-explore-mapview-maplayerprioritybuilder-class. This class instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapLayerPriorityBuilder renderedLast();</code></pre>
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
<li class="self-crumb">renderedLast abstract method</li>
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



</div>
`
}</HTMLBlock>
