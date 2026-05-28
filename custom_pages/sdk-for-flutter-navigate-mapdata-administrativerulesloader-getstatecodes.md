---
title: "getStateCodes abstract method"
slug: "sdk-for-flutter-navigate-mapdata-administrativerulesloader-getstatecodes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getStateCodes.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li>/sdk-for-flutter-navigate-mapdata-administrativerulesloader-class</li>
<li class="self-crumb">getStateCodes abstract method</li>
</ol>
<div class="self-name">getStateCodes</div>
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
<div class="main-content" data-above-sidebar="mapdata/AdministrativeRulesLoader-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>getStateCodes abstract method</h1></div>
<section class="multi-line-signature">
List&lt;<wbr/>String&gt;
getStateCodes(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-countrycode countryCode</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Synchronously loads the list of state codes from a specified country for which
administrative rules are availabe.</p>
<p>These state codes can then be used to get specific
administrative rules for a specified state using the <code>get_administrative_rules()</code> method.
Returns a list with all the state codes available in the country. In case the country has no
states, the list will be empty.</p>
<ul>
<li><code>countryCode</code> The country code for which the state codes are going to be retrieved.</li>
</ul>
<p>Returns <code>List&lt;String&gt;</code>. The list of state codes present in the country for which administrative rules
are available.</p>
<p>Throws if it's not possible to return the list of state codes.</p>
<p>Throws /sdk-for-flutter-navigate-mapdata-mapdataloaderexceptionexception-class. Specifies reason, why the list of state codes was not returned.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;String&gt; getStateCodes(CountryCode countryCode);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li>/sdk-for-flutter-navigate-mapdata-administrativerulesloader-class</li>
<li class="self-crumb">getStateCodes abstract method</li>
</ol>
<h5>AdministrativeRulesLoader class</h5>
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
