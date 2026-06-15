---
title: "hashCode property"
slug: "sdk-for-flutter-navigate-core-engine-sdkoptions-hashcode"
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
that affects <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-operator-equals">operator ==</a> comparisons.</p>
<p>All objects have hash codes.
The default hash code implemented by <code>Object</code>
represents only the identity of the object,
the same way as the default <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-operator-equals">operator ==</a> implementation only considers objects
equal if they are identical (see <code>identityHashCode</code>).</p>
<p>If <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-operator-equals">operator ==</a> is overridden to use the object state instead,
the hash code must also be changed to represent that state,
otherwise the object cannot be used in hash based data structures
like the default <code>Set</code> and <code>Map</code> implementations.</p>
<p>Hash codes must be the same for objects that are equal to each other
according to <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-operator-equals">operator ==</a>.
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
<p>If a subclass overrides <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-hashcode">hashCode</a>, it should override the
<a href="sdk-for-flutter-navigate-core-engine-sdkoptions-operator-equals">operator ==</a> operator as well to maintain consistency.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@override
int get hashCode {
  int result = 7;
  result = 31 * result + scope.hashCode;
  result = 31 * result + cachePath.hashCode;
  result = 31 * result + cacheSizeInBytes.hashCode;
  result = 31 * result + dataPath.hashCode;
  result = 31 * result + persistentMapStoragePath.hashCode;
  result = 31 * result + politicalView.hashCode;
  result = 31 * result + offlineMode.hashCode;
  result = 31 * result + layerConfiguration.hashCode;
  result = 31 * result + DeepCollectionEquality().hash(catalogConfigurations);
  result = 31 * result + autoUpdateOfOnlineCache.hashCode;
  result = 31 * result + DeepCollectionEquality().hash(customEngineOptions);
  result = 31 * result + actionOnCacheLock.hashCode;
  result = 31 * result + authenticationMode.hashCode;
  result = 31 * result + networkSettings.hashCode;
  result = 31 * result + lowMemoryMode.hashCode;
  result = 31 * result + billingTag.hashCode;
  result = 31 * result + customOptions.hashCode;
  return result;
}</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
