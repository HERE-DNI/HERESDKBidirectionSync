---
title: "getAdministrativeRules abstract method"
slug: "sdk-for-flutter-navigate-mapdata-administrativerulesloader-getadministrativerules"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getAdministrativeRules.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li>/sdk-for-flutter-navigate-mapdata-administrativerulesloader-class</li>
<li class="self-crumb">getAdministrativeRules abstract method</li>
</ol>
<div class="self-name">getAdministrativeRules</div>
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
<h1>getAdministrativeRules abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-mapdata-administrativerules-class
getAdministrativeRules(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-countrycode countryCode, </li>
<li>String? stateCode</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Synchronously load the administrative rules for the specified country and state.</p>
<p><strong>Note:</strong> The <code>state_code</code> parameter can be set to <code>null</code>. In this case, even if the country has multiple states, each with
their own administrative rules, an /sdk-for-flutter-navigate-mapdata-administrativerules-class object will be returned, containing the administrative
rules valid for the entire country. These rules can however be overwritten by the state rules when the driver is in that
specific state, so it is recommended to always retrieve the rules for a specific state for higher accuracy.
Returns an /sdk-for-flutter-navigate-mapdata-administrativerules-class object which contains the administrative rules for the specified country and
state.</p>
<ul>
<li>
<p><code>countryCode</code> The country code for which the administrative rules will be retrieved.</p>
</li>
<li>
<p><code>stateCode</code> The state name for which the administrative rules will be received. It can be <code>null</code>.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-mapdata-administrativerules-class. Requested administrative rules for the country and the state specified.</p>
<p>Throws /sdk-for-flutter-navigate-mapdata-mapdataloaderexceptionexception-class. Specifies reason, why the administrative rules were not retrieved.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">AdministrativeRules getAdministrativeRules(CountryCode countryCode, String? stateCode);</code></pre>
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
<li class="self-crumb">getAdministrativeRules abstract method</li>
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
