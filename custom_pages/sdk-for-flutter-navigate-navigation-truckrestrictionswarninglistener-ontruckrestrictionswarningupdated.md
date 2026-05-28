---
title: "onTruckRestrictionsWarningUpdated abstract method"
slug: "sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-ontruckrestrictionswarningupdated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onTruckRestrictionsWarningUpdated.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class</li>
<li class="self-crumb">onTruckRestrictionsWarningUpdated abstract method</li>
</ol>
<div class="self-name">onTruckRestrictionsWarningUpdated</div>
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
<div class="main-content" data-above-sidebar="navigation/TruckRestrictionsWarningListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>onTruckRestrictionsWarningUpdated abstract method</h1></div>
<section class="multi-line-signature">
void
onTruckRestrictionsWarningUpdated(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-class&gt; restrictions</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Called whenever the distance type (/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-distancetype) of a truck
restriction changes.</p>
<p>If needed, it is up to the application to maintain a list of active
warnings like the ones with /sdk-for-flutter-navigate-navigation-distancetype or /sdk-for-flutter-navigate-navigation-distancetype based on the
updates provided by this method.</p>
<ul>
<li><code>restrictions</code> A list containing truck restriction warnings that have their distance
type (/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-distancetype) updated.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onTruckRestrictionsWarningUpdated(List&lt;TruckRestrictionWarning&gt; restrictions);</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class</li>
<li class="self-crumb">onTruckRestrictionsWarningUpdated abstract method</li>
</ol>
<h5>TruckRestrictionsWarningListener class</h5>
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
