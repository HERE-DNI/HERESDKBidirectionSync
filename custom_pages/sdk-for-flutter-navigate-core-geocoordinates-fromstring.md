---
title: "fromString static method"
slug: "sdk-for-flutter-navigate-core-geocoordinates-fromstring"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- fromString.html -->


<div>
<h1>fromString static method</h1></div>

<a href="/sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>?
fromString(<ol class="parameter-list single-line"> <li>String input</li>
</ol>)

      

    

<p>Constructs GeoCoordinates from the provided string in specified format.</p>
<p>Corrects values of lat and long if they exceed the ranges.
If the latitude value is out of range of [-90.0, 90.0] it's clamped to that range.
If the longitude value is out of range of [-180.0, 180.0] it's replaced with a value
within the range, representing effectively the same meridian.
Examples: <code>53.43762,-13.65468</code>.
<code>49°59'56.948"N, 15°48'22.989"E</code>
<code>50d4m17.698N 14d24m2.826E</code>
<code>49.9991522N, 150.8063858E</code>
<code>40°26′47″N 79°58′36″W</code></p>
<ul>
<li><code>input</code> String representing GeoCoordinates in one of supported formats.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates?</a>. Created GeoCoordinates, or 'null' if string was not in appropriate format.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static GeoCoordinates? fromString(String input) =&gt; $prototype.fromString(input);</code></pre>

 



</div>
`
}</HTMLBlock>
