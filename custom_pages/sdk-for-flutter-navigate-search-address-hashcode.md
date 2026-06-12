---
title: "hashCode property"
slug: "sdk-for-flutter-navigate-search-address-hashcode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- hashCode.html -->


<div>
<h1>hashCode property</h1></div>
<section id="getter">

<div>
<ol class="annotation-list">
<li>@override</li>
</ol>
</div>
int
hashCode


<p>The hash code for this object.</p>
<p>A hash code is a single integer which represents the state of the object
that affects <a href="/sdk-for-flutter-navigate-search-address-operator-equals">operator ==</a> comparisons.</p>
<p>All objects have hash codes.
The default hash code implemented by <code>Object</code>
represents only the identity of the object,
the same way as the default <a href="/sdk-for-flutter-navigate-search-address-operator-equals">operator ==</a> implementation only considers objects
equal if they are identical (see <code>identityHashCode</code>).</p>
<p>If <a href="/sdk-for-flutter-navigate-search-address-operator-equals">operator ==</a> is overridden to use the object state instead,
the hash code must also be changed to represent that state,
otherwise the object cannot be used in hash based data structures
like the default <code>Set</code> and <code>Map</code> implementations.</p>
<p>Hash codes must be the same for objects that are equal to each other
according to <a href="/sdk-for-flutter-navigate-search-address-operator-equals">operator ==</a>.
The hash code of an object should only change if the object changes
in a way that affects equality.
There are no further requirements for the hash codes.
They need not be consistent between executions of the same program
and there are no distribution guarantees.</p>
<p>Objects that are not equal are allowed to have the same hash code.
It is even technically allowed that all instances have the same hash code,
but if clashes happen too often,
it may reduce the efficiency of hash-based data structures
like <code>HashSet</code> or <code>HashMap</code>.</p>
<p>If a subclass overrides <a href="/sdk-for-flutter-navigate-search-address-hashcode">hashCode</a>, it should override the
<a href="/sdk-for-flutter-navigate-search-address-operator-equals">operator ==</a> operator as well to maintain consistency.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@override
int get hashCode {
  int result = 7;
  result = 31 * result + city.hashCode;
  result = 31 * result + countryCode.hashCode;
  result = 31 * result + country.hashCode;
  result = 31 * result + district.hashCode;
  result = 31 * result + subdistrict.hashCode;
  result = 31 * result + houseNumOrName.hashCode;
  result = 31 * result + postalCode.hashCode;
  result = 31 * result + state.hashCode;
  result = 31 * result + county.hashCode;
  result = 31 * result + street.hashCode;
  result = 31 * result + block.hashCode;
  result = 31 * result + subBlock.hashCode;
  result = 31 * result + addressText.hashCode;
  result = 31 * result + type.hashCode;
  result = 31 * result + stateCode.hashCode;
  return result;
}</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
