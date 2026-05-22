---
title: "Untitled"
slug: "sdk-for-flutter-explore-routing-scooteroptions-allowhighway"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- allowHighway.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-scooteroptions-class</li>
<li class="self-crumb">allowHighway property</li>
</ol>
<div class="self-name">allowHighway</div>
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
<div class="main-content" data-above-sidebar="routing/ScooterOptions-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>allowHighway property</h1></div>
<section class="multi-line-signature">
        
        bool
        allowHighway
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Specifies whether scooter is allowed on highway or not. <code>True</code> means scooter is
allowed to use highways and <code>false</code> means otherwise. By default it is set to <code>false</code>.
Note that there is a similar parameter in /sdk-for-flutter-explore-routing-avoidanceoptions-class, to
disallow highway usage, see /sdk-for-flutter-explore-routing-roadfeatures.
As the avoidance options takes precedence, if this parameter is also used, then
scooters are not allowed to use highways even if <code>allowHighway</code> is set to <code>true</code>.
However, if no alternative route is possible, the calculated route may use highways.
In such a case, a /sdk-for-flutter-explore-routing-sectionnotice-class will be provided in the related /sdk-for-flutter-explore-routing-section-class
to indicate that the highway usage restriction is violated on this route.
A few examples:</p>
<p>1 - If no avoidance option is set, and <code>allowHighway = false</code>, when no route is found without
highway usage, a notice is received.</p>
<p>2 - If no avoidance option is set, and <code>allowHighway = true</code>, when no route is found without
highway usage, no notice is received.</p>
<p>3 - If only <code>avoid[features] = controlledAccessHighway</code> is set, when no route is found without
highway usage, a notice is received.</p>
<p>4 - If both <code>avoid[features] = controlledAccessHighway</code> and <code>allowHighway = true</code> are set,
when no route is found without highway usage, a notice is received.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool allowHighway;</code></pre>
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
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-scooteroptions-class</li>
<li class="self-crumb">allowHighway property</li>
</ol>
<h5>ScooterOptions class</h5>
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
