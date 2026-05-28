---
title: "getWarningNotificationDistances abstract method"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-getwarningnotificationdistances"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getWarningNotificationDistances.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-navigatorinterface-class</li>
<li class="self-crumb">getWarningNotificationDistances abstract method</li>
</ol>
<div class="self-name">getWarningNotificationDistances</div>
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
<div class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>getWarningNotificationDistances abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-navigation-warningnotificationdistances-class
getWarningNotificationDistances(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-warningtype warningType</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Returns the warning notification distances for the requested warning type.</p>
<p>The return value can be used as the
base for configuring warning notification distances. Configure the relevant attributes of this object according
to your preferences, and then set it by calling <code>setWarningNotificationDistances</code> function with the same
warning type and the modified warning notification distances object.</p>
<ul>
<li><code>warningType</code> The warning type for which the notification distances will be returned.</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-navigation-warningnotificationdistances-class. The notification distances for the given warning type.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">WarningNotificationDistances getWarningNotificationDistances(WarningType warningType);</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-navigatorinterface-class</li>
<li class="self-crumb">getWarningNotificationDistances abstract method</li>
</ol>
<h5>NavigatorInterface class</h5>
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
