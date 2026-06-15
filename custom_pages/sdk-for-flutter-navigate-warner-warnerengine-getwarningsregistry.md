---
title: "getWarningsRegistry abstract method"
slug: "sdk-for-flutter-navigate-warner-warnerengine-getwarningsregistry"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getWarningsRegistry.html -->


<div>
<h1>getWarningsRegistry abstract method</h1></div>

<a href="sdk-for-flutter-navigate-warner-warningsregistry-class">WarningsRegistry</a>
getWarningsRegistry()

      

    

<p>Returns the centralized access point for retrieving full metadata of any supported
warning category (e.g., safety cameras, truck restrictions, etc.).</p>
<p><a href="sdk-for-flutter-navigate-warner-warningsregistry-class">WarningsRegistry</a> class exposes getter methods, each returning the detailed warning object for the given identifier.
Use this getter to look up complete warning information by its id, as provided through <code>WarningListener.onWarning</code>.</p>
<p>Returns <a href="sdk-for-flutter-navigate-warner-warningsregistry-class">WarningsRegistry</a>. The centralized <a href="sdk-for-flutter-navigate-warner-warningsregistry-class">WarningsRegistry</a> instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">WarningsRegistry getWarningsRegistry();</code></pre>

 



</div>
`
}</HTMLBlock>
