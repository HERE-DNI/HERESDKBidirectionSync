---
title: "confirmHEREPrivacyNoticeInclusion abstract method"
slug: "sdk-for-flutter-navigate-location-locationenginebase-confirmhereprivacynoticeinclusion"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- confirmHEREPrivacyNoticeInclusion.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationenginebase-class</li>
<li class="self-crumb">confirmHEREPrivacyNoticeInclusion abstract method</li>
</ol>
<div class="self-name">confirmHEREPrivacyNoticeInclusion</div>
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
<div class="main-content" data-above-sidebar="location/LocationEngineBase-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>confirmHEREPrivacyNoticeInclusion abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-location-confirmationstatus
confirmHEREPrivacyNoticeInclusion(<wbr/>)

      

    </section>
<section class="desc markdown">
<p>It is the responsibility of the application developer to ensure that
the application user is informed about the collection of characteristic information
regarding nearby mobile and Wi-Fi network signals.</p>
<p>Additionally, a link to the related
<a href="https://legal.here.com/en-gb/here-network-positioning-via-sdk">HERE Privacy Notice</a>
must be made available to the user.</p>
<p>This information can be included in the application's Terms &amp; Conditions,
Privacy Policy, or otherwise made accessible to the user.</p>
<p>An example text for informing users about the data collection:
"This application uses location services provided by HERE Technologies.
To maintain, improve, and provide these services, HERE Technologies occasionally collects
characteristic information about nearby mobile and Wi-Fi network signals.
For more information, please refer to the HERE Privacy Notice at:
<a href='https://legal.here.com/en-gb/here-network-positioning-via-sdk"'>https://legal.here.com/en-gb/here-network-positioning-via-sdk"</a></p>
<p><strong>Note:</strong> By calling this method, the application developer confirms that
this information is made available to the end user.</p>
<p>For example, it is sufficient to inform users once that using the app requires
acceptance of its terms (if any). Then, in the terms include the
above mentioned data collection information and a link to the related HERE Privacy Notice.
The user is not required to open the terms to acknowledge the data collection details.
The "Positioning" example app on <a href="https://github.com/heremaps/here-sdk-examples">GitHub</a>
provides an example of this.</p>
<p>When the above criteria are met, it is recommended to silently execute this
method each time before starting the <code>LocationEngine</code>, as failure to do so
will result in the engine being non-functional.</p>
<p>It is not necessary to call this method on the iOS platform.</p>
<p>Returns /sdk-for-flutter-navigate-location-confirmationstatus. Immediately returns with /sdk-for-flutter-navigate-location-confirmationstatus.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ConfirmationStatus confirmHEREPrivacyNoticeInclusion();</code></pre>
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
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationenginebase-class</li>
<li class="self-crumb">confirmHEREPrivacyNoticeInclusion abstract method</li>
</ol>
<h5>LocationEngineBase class</h5>
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
