---
title: "Untitled"
slug: "sdk-for-flutter-navigate-search-evchargingtruckrestriction-truckaccess"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- truckAccess.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-search-evchargingtruckrestriction-class</li>
<li class="self-crumb">truckAccess property</li>
</ol>
<div class="self-name">truckAccess</div>
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
<div class="main-content" data-above-sidebar="search/EVChargingTruckRestriction-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>truckAccess property</h1></div>
<section class="multi-line-signature">
        
        List&lt;<wbr/>/sdk-for-flutter-navigate-transport-truckclass&gt;
truckAccess
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Access categories for trucks and light commercial vehicles that the
EV charging location is designed to serve.</p>
<p>While the classifications used as basis for the categories are solely based on vehicle mass,
in EV charging context they can be interpreted to give an idea of the dimensional class too,
as well as possible other restrictions set by the operator. If there are true dimensional or
weight limits at the EV charging location, they are specified separately in vehicleLimitations.</p>
<p>The classification is available only to a subset of EV charging locations, depending on the
information available from the operators. Hence, at least vehicles belonging to the
/sdk-for-flutter-navigate-transport-truckclass category can be charged also in many EV charging locations not having
explicit signaling for the /sdk-for-flutter-navigate-transport-truckclass category.</p>
<p>Furthermore, although the classification is based on mass/weight ranges in growing order,
an upper class does not automatically mean that also all lower class vehicles are welcome to charge.
For example, a location marked only with category /sdk-for-flutter-navigate-transport-truckclass
is reserved for long-haul trucks only.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;TruckClass&gt; truckAccess;</code></pre>
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
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-search-evchargingtruckrestriction-class</li>
<li class="self-crumb">truckAccess property</li>
</ol>
<h5>EVChargingTruckRestriction class</h5>
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
