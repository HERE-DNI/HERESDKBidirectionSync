---
title: "getPreferredValueForLocales method"
slug: "sdk-for-flutter-explore-routing-localizedroadnumbers-getpreferredvalueforlocales"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getPreferredValueForLocales.html -->


<div>
<h1>getPreferredValueForLocales method</h1></div>

String?
getPreferredValueForLocales(<ol class="parameter-list single-line"> <li>List&lt;<a href="https://pub.dev/documentation/intl/0.20.2/locale/Locale-class.html">Locale</a>&gt; locales</li>
</ol>)

      

    

<p>Returns best name or title to be presented to the user according to specified
locales.</p>
<p>The locales are expected to be ordered by priority.
If no matching locale found - the default is returned.
In case of empty list returns <code>null</code>.</p>
<ul>
<li><code>locales</code> Locales</li>
</ul>
<p>Returns <code>String?</code>. The best name or title to be presented to the user according to specified locales,
default or <code>null</code> if list is empty.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String? getPreferredValueForLocales(List&lt;Locale&gt; locales) =&gt; $prototype.getPreferredValueForLocales(this, locales);</code></pre>

 



</div>
`
}</HTMLBlock>
