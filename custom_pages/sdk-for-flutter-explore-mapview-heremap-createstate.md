---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-heremap-createstate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- createState.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-heremap-class</li>
<li class="self-crumb">createState method</li>
</ol>
<div class="self-name">createState</div>
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
<div class="main-content" data-above-sidebar="mapview/HereMap-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>createState method</h1></div>
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@override</li>
</ol>
</div>
State&lt;<wbr/>StatefulWidget&gt;
createState(<wbr/>)

      

    </section>
<section class="desc markdown">
<p>Creates the mutable state for this widget at a given location in the tree.</p>
<p>Subclasses should override this method to return a newly created
instance of their associated <code>State</code> subclass:</p>
<pre class="language-dart"><code class="language-dart">@override
State&lt;SomeWidget&gt; createState() =&gt; _SomeWidgetState();
</code></pre>
<p>The framework can call this method multiple times over the lifetime of
a <code>StatefulWidget</code>. For example, if the widget is inserted into the tree
in multiple locations, the framework will create a separate <code>State</code> object
for each location. Similarly, if the widget is removed from the tree and
later inserted into the tree again, the framework will call /sdk-for-flutter-explore-mapview-heremap-createstate
again to create a fresh <code>State</code> object, simplifying the lifecycle of
<code>State</code> objects.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@override
State&lt;StatefulWidget&gt; createState() =&gt; _HereMapState();</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-heremap-class</li>
<li class="self-crumb">createState method</li>
</ol>
<h5>HereMap class</h5>
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
