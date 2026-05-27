---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-span-getshieldtext"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- getShieldText.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/Span-class.html">/sdk-for-flutter-explore-routing-span-class</a></li>
<li class="self-crumb">getShieldText abstract method</li>
</ol>
<div class="self-name">getShieldText</div>
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
<div class="main-content" data-above-sidebar="routing/Span-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>getShieldText abstract method</h1></div>
<section class="multi-line-signature">
String
getShieldText(<wbr/><ol class="parameter-list single-line"> <li><a href="../../routing/LocalizedRoadNumber-class.html">/sdk-for-flutter-explore-routing-localizedroadnumber-class</a> roadNumber</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Converts full route number to the value to be displayed on the road shield.</p>
<p>The results are based on country code and state code of <code>Span</code> object and route type of passed <code>road_number</code> argument.</p>
<ul>
<li><code>roadNumber</code> Route number to convert to shield text.</li>
</ul>
<p>Returns <code>String</code>. Text on the road shield to display.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String getShieldText(LocalizedRoadNumber roadNumber);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/Span-class.html">/sdk-for-flutter-explore-routing-span-class</a></li>
<li class="self-crumb">getShieldText abstract method</li>
</ol>
<h5>Span class</h5>
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
</HTMLBlock>
