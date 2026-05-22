---
title: "Untitled"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-electronichorizonoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonOptions.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-class</li>
<li class="self-crumb">ElectronicHorizonOptions constructor</li>
</ol>
<div class="self-name">ElectronicHorizonOptions</div>
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
<div class="main-content" data-above-sidebar="electronic_horizon/ElectronicHorizonOptions-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>ElectronicHorizonOptions constructor</h1></div>
<section class="multi-line-signature">
ElectronicHorizonOptions(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>double&gt; lookAheadDistancesInMeters, </li>
<li>double trailingDistanceInMeters</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<p>Offline availability: This property is available online and offline.</p>
<ul>
<li><code>lookAheadDistancesInMeters</code> The ordered list of distances that define how far to look ahead in meters when calculating electronic horizon paths.
The first entry of the list is for the most preferred path, the second is for the side paths of the first level,
the third is for the side paths of the second level, and so on. Each entry defines how far ahead the path should be provided.
The valid number of values is from one to ten. Values beyond the tenth entry are removed from the list.
If the list is empty, a single default distance value is used instead.</li>
<li><code>trailingDistanceInMeters</code> The trailing distance of the electronic horizon path in meters.
Segments are removed from the path once they are passed and the distance to them exceeds this value.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ElectronicHorizonOptions(this.lookAheadDistancesInMeters, this.trailingDistanceInMeters);</code></pre>
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
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-class</li>
<li class="self-crumb">ElectronicHorizonOptions constructor</li>
</ol>
<h5>ElectronicHorizonOptions class</h5>
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
