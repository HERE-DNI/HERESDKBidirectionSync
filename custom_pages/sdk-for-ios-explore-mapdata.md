---
title: "MapData  Reference"
slug: "sdk-for-ios-explore-mapdata"
---

<span id="//apple_ref/swift/Section/MapData" class="dashAnchor"></span>

<div class="content-wrapper">

<a href="sdk-for-ios-explore-index">heresdk</a> <img src="img/carat.png" id="sdk-for-ios-explore-carat" /> MapData Reference

</div>

<div class="content-wrapper">

<nav class="sidebar">

- <a href="sdk-for-ios-explore-core">Core</a>
  - <a href="sdk-for-ios-explore-structs-anchor2d">Anchor2D</a>
  - <a href="sdk-for-ios-explore-structs-anchor2dkeyframe">Anchor2DKeyframe</a>
  - <a href="sdk-for-ios-explore-classes-angle">Angle</a>
  - <a href="sdk-for-ios-explore-structs-anglerange">AngleRange</a>
  - <a href="sdk-for-ios-explore-classes-authentication">Authentication</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk31AuthenticationCompletionHandlera">AuthenticationCompletionHandler</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk23AuthenticationExceptiona">AuthenticationException</a>
  - <a href="sdk-for-ios-explore-classes-authenticationmode">AuthenticationMode</a>
  - <a href="sdk-for-ios-explore-structs-brandlogo">BrandLogo</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk30CacheCallbackCompletionHandlera">CacheCallbackCompletionHandler</a>
  - <a href="sdk-for-ios-explore-enums-cardinaldirection">CardinalDirection</a>
  - <a href="sdk-for-ios-explore-structs-catalogconfiguration">CatalogConfiguration</a>
  - <a href="sdk-for-ios-explore-structs-catalogidentifier">CatalogIdentifier</a>
  - <a href="sdk-for-ios-explore-enums-catalogtype">CatalogType</a>
  - <a href="sdk-for-ios-explore-classes-catalogupdatetask">CatalogUpdateTask</a>
  - <a href="sdk-for-ios-explore-classes-catalogversionhint">CatalogVersionHint</a>
  - <a href="sdk-for-ios-explore-classes-collectionof">CollectionOf</a>
  - <a href="sdk-for-ios-explore-enums-countrycode">CountryCode</a>
  - <a href="sdk-for-ios-explore-enums-currenttype">CurrentType</a>
  - <a href="sdk-for-ios-explore-protocols-custommetadatavalue">CustomMetadataValue</a>
  - <a href="sdk-for-ios-explore-structs-desiredcatalog">DesiredCatalog</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk14DeviceIdHandlea">DeviceIdHandle</a>
  - <a href="sdk-for-ios-explore-enums-enginebaseurl">EngineBaseURL</a>
  - <a href="sdk-for-ios-explore-structs-engineoptions">EngineOptions</a>
  - <a href="sdk-for-ios-explore-structs-externalid">ExternalID</a>
  - <a href="sdk-for-ios-explore-structs-geobox">GeoBox</a>
  - <a href="sdk-for-ios-explore-structs-geocircle">GeoCircle</a>
  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-explore-structs-geocoordinatesupdate">GeoCoordinatesUpdate</a>
  - <a href="sdk-for-ios-explore-structs-geocorridor">GeoCorridor</a>
  - <a href="sdk-for-ios-explore-structs-geoorientation">GeoOrientation</a>
  - <a href="sdk-for-ios-explore-structs-geoorientationupdate">GeoOrientationUpdate</a>
  - <a href="sdk-for-ios-explore-structs-geopolygon">GeoPolygon</a>
  - <a href="sdk-for-ios-explore-structs-geopolyline">GeoPolyline</a>
  - <a href="sdk-for-ios-explore-enums-geopolylinedirection">GeoPolylineDirection</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk18InstantiationErrora">InstantiationError</a>
  - <a href="sdk-for-ios-explore-enums-instantiationerrorcode">InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-structs-integerrange">IntegerRange</a>
  - <a href="sdk-for-ios-explore-enums-junctionstraversability">JunctionsTraversability</a>
  - <a href="sdk-for-ios-explore-enums-languagecode">LanguageCode</a>
  - <a href="sdk-for-ios-explore-structs-layerconfiguration">LayerConfiguration</a>
  - <a href="sdk-for-ios-explore-structs-layerconfiguration-feature">– Feature</a>
  - <a href="sdk-for-ios-explore-structs-localizedroadnumber">LocalizedRoadNumber</a>
  - <a href="sdk-for-ios-explore-structs-localizedroadnumbers">LocalizedRoadNumbers</a>
  - <a href="sdk-for-ios-explore-structs-localizedtext">LocalizedText</a>
  - <a href="sdk-for-ios-explore-structs-localizedtexts">LocalizedTexts</a>
  - <a href="sdk-for-ios-explore-structs-location">Location</a>
  - <a href="sdk-for-ios-explore-protocols-locationdelegate">LocationDelegate</a>
  - <a href="sdk-for-ios-explore-enums-locationsource">LocationSource</a>
  - <a href="sdk-for-ios-explore-enums-locationtechnology">LocationTechnology</a>
  - <a href="sdk-for-ios-explore-structs-locationtime">LocationTime</a>
  - <a href="sdk-for-ios-explore-protocols-logappender">LogAppender</a>
  - <a href="sdk-for-ios-explore-classes-logcontrol">LogControl</a>
  - <a href="sdk-for-ios-explore-enums-loglevel">LogLevel</a>
  - <a href="sdk-for-ios-explore-classes-metadata">Metadata</a>
  - <a href="sdk-for-ios-explore-enums-metadatatype">MetadataType</a>
  - <a href="sdk-for-ios-explore-structs-nameid">NameID</a>
  - <a href="sdk-for-ios-explore-structs-networkendpoint">NetworkEndpoint</a>
  - <a href="sdk-for-ios-explore-structs-networksettings">NetworkSettings</a>
  - <a href="sdk-for-ios-explore-structs-parameterconfiguration">ParameterConfiguration</a>
  - <a href="sdk-for-ios-explore-enums-passthroughfeature">PassThroughFeature</a>
  - <a href="sdk-for-ios-explore-enums-powertype">PowerType</a>
  - <a href="sdk-for-ios-explore-structs-pedestrianprofile">PedestrianProfile</a>
  - <a href="sdk-for-ios-explore-structs-pickedplace">PickedPlace</a>
  - <a href="sdk-for-ios-explore-protocols-platformthreading">PlatformThreading</a>
  - <a href="sdk-for-ios-explore-structs-point2d">Point2D</a>
  - <a href="sdk-for-ios-explore-structs-point3d">Point3D</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk39PolylineSimplificationCompletionHandlera">PolylineSimplificationCompletionHandler</a>
  - <a href="sdk-for-ios-explore-enums-polylinesimplificationerror">PolylineSimplificationError</a>
  - <a href="sdk-for-ios-explore-classes-polylinesimplifier">PolylineSimplifier</a>
  - <a href="sdk-for-ios-explore-classes-polylinesimplifier-options">– Options</a>
  - <a href="sdk-for-ios-explore-structs-proxysettings">ProxySettings</a>
  - <a href="sdk-for-ios-explore-structs-proxysettings-proxytype">– ProxyType</a>
  - <a href="sdk-for-ios-explore-structs-proxysettings-credentials">– Credentials</a>
  - <a href="sdk-for-ios-explore-structs-rectangle2d">Rectangle2D</a>
  - <a href="sdk-for-ios-explore-enums-routetype">RouteType</a>
  - <a href="sdk-for-ios-explore-protocols-runnable">Runnable</a>
  - <a href="sdk-for-ios-explore-classes-sdkbuildinformation">SDKBuildInformation</a>
  - <a href="sdk-for-ios-explore-classes-sdkcache">SDKCache</a>
  - <a href="sdk-for-ios-explore-classes-sdkinternalinitializer">SDKInternalInitializer</a>
  - <a href="sdk-for-ios-explore-classes-sdklogger">SDKLogger</a>
  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>
  - <a href="sdk-for-ios-explore-classes-sdknativeengine-purgememorystrategy">– PurgeMemoryStrategy</a>
  - <a href="sdk-for-ios-explore-core#/c:@M@heresdk@objc(cs">SDKNativeEngineHolder</a>SDKNativeEngineHolder)
  - <a href="sdk-for-ios-explore-structs-sdkoptions">SDKOptions</a>
  - <a href="sdk-for-ios-explore-structs-sdkversion">SDKVersion</a>
  - <a href="sdk-for-ios-explore-structs-size2d">Size2D</a>
  - <a href="sdk-for-ios-explore-core#/s:SS">String</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>
  - <a href="sdk-for-ios-explore-enums-taskoutcome">TaskOutcome</a>
  - <a href="sdk-for-ios-explore-classes-threading">Threading</a>
  - <a href="sdk-for-ios-explore-classes-timerule">TimeRule</a>
  - <a href="sdk-for-ios-explore-structs-transportprofile">TransportProfile</a>
  - <a href="sdk-for-ios-explore-extensions-uicolor">UIColor</a>
  - <a href="sdk-for-ios-explore-enums-unitsystem">UnitSystem</a>
  - <a href="sdk-for-ios-explore-structs-usagestats">UsageStats</a>
  - <a href="sdk-for-ios-explore-structs-usagestats-feature">– Feature</a>
  - <a href="sdk-for-ios-explore-structs-usagestats-networkstats">– NetworkStats</a>
- <a href="sdk-for-ios-explore-electronichorizon">ElectronicHorizon</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizon">ElectronicHorizon</a>
  - <a href="sdk-for-ios-explore-classes-electronichorizondataloader">ElectronicHorizonDataLoader</a>
  - <a href="sdk-for-ios-explore-enums-electronichorizondataloadererrorcode">ElectronicHorizonDataLoaderErrorCode</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizondataloaderresult">ElectronicHorizonDataLoaderResult</a>
  - <a href="sdk-for-ios-explore-enums-electronichorizondataloadedstatus">ElectronicHorizonDataLoadedStatus</a>
  - <a href="sdk-for-ios-explore-protocols-electronichorizondataloaderstatusdelegate">ElectronicHorizonDataLoaderStatusDelegate</a>
  - <a href="sdk-for-ios-explore-protocols-electronichorizondelegate">ElectronicHorizonDelegate</a>
  - <a href="sdk-for-ios-explore-classes-electronichorizonengine">ElectronicHorizonEngine</a>
  - <a href="sdk-for-ios-explore-enums-electronichorizonerrorcode">ElectronicHorizonErrorCode</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonoptions">ElectronicHorizonOptions</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonpath">ElectronicHorizonPath</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonposition">ElectronicHorizonPosition</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonsegment">ElectronicHorizonSegment</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonsegmentchanges">ElectronicHorizonSegmentChanges</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonsegmentid">ElectronicHorizonSegmentId</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonupdate">ElectronicHorizonUpdate</a>
- <a href="sdk-for-ios-explore-ev">EV</a>
  - <a href="sdk-for-ios-explore-enums-evchargingconnectorformat">EVChargingConnectorFormat</a>
  - <a href="sdk-for-ios-explore-structs-evchargingconnectortype">EVChargingConnectorType</a>
  - <a href="sdk-for-ios-explore-enums-evsecapability">EVSECapability</a>
  - <a href="sdk-for-ios-explore-enums-evsepaymentsupport">EVSEPaymentSupport</a>
  - <a href="sdk-for-ios-explore-enums-evsestate">EVSEState</a>
- <a href="sdk-for-ios-explore-positioning">Positioning</a>
  - <a href="sdk-for-ios-explore-structs-authenticationdata">AuthenticationData</a>
  - <a href="sdk-for-ios-explore-enums-authenticationerror">AuthenticationError</a>
  - <a href="sdk-for-ios-explore-enums-confirmationstatus">ConfirmationStatus</a>
  - <a href="sdk-for-ios-explore-enums-locationaccuracy">LocationAccuracy</a>
  - <a href="sdk-for-ios-explore-protocols-locationenginebase">LocationEngineBase</a>
  - <a href="sdk-for-ios-explore-enums-locationenginestatus">LocationEngineStatus</a>
  - <a href="sdk-for-ios-explore-enums-locationfeature">LocationFeature</a>
  - <a href="sdk-for-ios-explore-classes-locationengine">LocationEngine</a>
  - <a href="sdk-for-ios-explore-classes-locationsimulator">LocationSimulator</a>
  - <a href="sdk-for-ios-explore-structs-locationsimulatoroptions">LocationSimulatorOptions</a>
  - <a href="sdk-for-ios-explore-protocols-locationstatusdelegate">LocationStatusDelegate</a>
- <a href="sdk-for-ios-explore-mapdata">MapData</a>
  - <a href="sdk-for-ios-explore-structs-administrativerules">AdministrativeRules</a>
  - <a href="sdk-for-ios-explore-classes-administrativerulesloader">AdministrativeRulesLoader</a>
  - <a href="sdk-for-ios-explore-structs-allowedtransportmodes">AllowedTransportModes</a>
  - <a href="sdk-for-ios-explore-structs-bloodalcoholcontentlimit">BloodAlcoholContentLimit</a>
  - <a href="sdk-for-ios-explore-structs-connectivity">Connectivity</a>
  - <a href="sdk-for-ios-explore-structs-directedocmsegmentid">DirectedOCMSegmentId</a>
  - <a href="sdk-for-ios-explore-structs-downloadingfileoptions">DownloadingFileOptions</a>
  - <a href="sdk-for-ios-explore-enums-drivingside">DrivingSide</a>
  - <a href="sdk-for-ios-explore-structs-filereference">FileReference</a>
  - <a href="sdk-for-ios-explore-enums-filereferencetype">FileReferenceType</a>
  - <a href="sdk-for-ios-explore-enums-headlightsrequirement">HeadlightsRequirement</a>
  - <a href="sdk-for-ios-explore-structs-laneattribute">LaneAttribute</a>
  - <a href="sdk-for-ios-explore-enums-localroadcharacteristic">LocalRoadCharacteristic</a>
  - <a href="sdk-for-ios-explore-mapdata#/s:7heresdk18MapDataLoaderErrora">MapDataLoaderError</a>
  - <a href="sdk-for-ios-explore-enums-mapdataloadererrorcode">MapDataLoaderErrorCode</a>
  - <a href="sdk-for-ios-explore-structs-ocmsegmentid">OCMSegmentId</a>
  - <a href="sdk-for-ios-explore-enums-parkingsideregulation">ParkingSideRegulation</a>
  - <a href="sdk-for-ios-explore-structs-physicalattributes">PhysicalAttributes</a>
  - <a href="sdk-for-ios-explore-structs-pretripplanning">PreTripPlanning</a>
  - <a href="sdk-for-ios-explore-structs-railwaycrossing">RailwayCrossing</a>
  - <a href="sdk-for-ios-explore-enums-railwaycrossingtype">RailwayCrossingType</a>
  - <a href="sdk-for-ios-explore-enums-roaddivider">RoadDivider</a>
  - <a href="sdk-for-ios-explore-structs-roadusages">RoadUsages</a>
  - <a href="sdk-for-ios-explore-structs-segmentconnectivities">SegmentConnectivities</a>
  - <a href="sdk-for-ios-explore-classes-segmentdata">SegmentData</a>
  - <a href="sdk-for-ios-explore-classes-segmentdataloader">SegmentDataLoader</a>
  - <a href="sdk-for-ios-explore-structs-segmentdataloaderoptions">SegmentDataLoaderOptions</a>
  - <a href="sdk-for-ios-explore-classes-segmentreferenceconverter">SegmentReferenceConverter</a>
  - <a href="sdk-for-ios-explore-classes-segmentspandata">SegmentSpanData</a>
  - <a href="sdk-for-ios-explore-structs-segmentspecialspeedsituation">SegmentSpecialSpeedSituation</a>
  - <a href="sdk-for-ios-explore-structs-segmentspeedlimit">SegmentSpeedLimit</a>
  - <a href="sdk-for-ios-explore-enums-specialspeedtype">SpecialSpeedType</a>
  - <a href="sdk-for-ios-explore-structs-tollcost">TollCost</a>
  - <a href="sdk-for-ios-explore-structs-tollpoint">TollPoint</a>
  - <a href="sdk-for-ios-explore-structs-tollstructure">TollStructure</a>
  - <a href="sdk-for-ios-explore-structs-tollstructuremaneuver">TollStructureManeuver</a>
  - <a href="sdk-for-ios-explore-enums-tollstructuretype">TollStructureType</a>
  - <a href="sdk-for-ios-explore-structs-tollsystem">TollSystem</a>
  - <a href="sdk-for-ios-explore-structs-trafficsignal">TrafficSignal</a>
  - <a href="sdk-for-ios-explore-enums-trafficsignallocation">TrafficSignalLocation</a>
  - <a href="sdk-for-ios-explore-enums-turnonredregulation">TurnOnRedRegulation</a>
- <a href="sdk-for-ios-explore-maploader">MapLoader</a>
  - <a href="sdk-for-ios-explore-structs-catalogupdateinfo">CatalogUpdateInfo</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk26CatalogsUpdateInfoCallbacka">CatalogsUpdateInfoCallback</a>
  - <a href="sdk-for-ios-explore-protocols-catalogupdateprogresslistener">CatalogUpdateProgressListener</a>
  - <a href="sdk-for-ios-explore-enums-catalogupdatestate">CatalogUpdateState</a>
  - <a href="sdk-for-ios-explore-enums-clientcertificaterequesttype">ClientCertificateRequestType</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk17CompletionHandlera">CompletionHandler</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk25ConfigureConnectionHandlea">ConfigureConnectionHandle</a>
  - <a href="sdk-for-ios-explore-protocols-dataattributesbase">DataAttributesBase</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk30DeleteRegionsCompletionHandlera">DeleteRegionsCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-downloadregionsstatuslistener">DownloadRegionsStatusListener</a>
  - <a href="sdk-for-ios-explore-classes-externalmapdatasourceclient">ExternalMapDataSourceClient</a>
  - <a href="sdk-for-ios-explore-enums-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk35ExternalMapDataSourceExceptionErrora">ExternalMapDataSourceExceptionError</a>
  - <a href="sdk-for-ios-explore-classes-externalmapdatasourceserver">ExternalMapDataSourceServer</a>
  - <a href="sdk-for-ios-explore-structs-installedcatalog">InstalledCatalog</a>
  - <a href="sdk-for-ios-explore-structs-installedregion">InstalledRegion</a>
  - <a href="sdk-for-ios-explore-enums-installedregionstatus">InstalledRegionStatus</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk8LineDataC">LineData</a>
  - <a href="sdk-for-ios-explore-classes-linedataaccessor">LineDataAccessor</a>
  - <a href="sdk-for-ios-explore-classes-linedatabuilder">LineDataBuilder</a>
  - <a href="sdk-for-ios-explore-classes-linedatasource">LineDataSource</a>
  - <a href="sdk-for-ios-explore-classes-linedatasourcebuilder">LineDataSourceBuilder</a>
  - <a href="sdk-for-ios-explore-enums-maploadererror">MapLoaderError</a>
  - <a href="sdk-for-ios-explore-classes-mapdownloader">MapDownloader</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk31MapDownloaderConstructionHandlea">MapDownloaderConstructionHandle</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk18MapLoaderExceptiona">MapLoaderException</a>
  - <a href="sdk-for-ios-explore-classes-mapdownloadertask">MapDownloaderTask</a>
  - <a href="sdk-for-ios-explore-protocols-mapupdateprogresslistener">MapUpdateProgressListener</a>
  - <a href="sdk-for-ios-explore-classes-mapupdater">MapUpdater</a>
  - <a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy">– MapUpdateVersionCommitPolicy</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk29MapUpdaterConstructionHandlera">MapUpdaterConstructionHandler</a>
  - <a href="sdk-for-ios-explore-classes-mapupdatetask">MapUpdateTask</a>
  - <a href="sdk-for-ios-explore-classes-mapversionhandle">MapVersionHandle</a>
  - <a href="sdk-for-ios-explore-enums-navigabilitytype">NavigabilityType</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk25OfflineStorageSizeHandlera">OfflineStorageSizeHandler</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk23RepairCompletionHandlera">RepairCompletionHandler</a>
  - <a href="sdk-for-ios-explore-structs-pemkeycertpair">PemKeyCertPair</a>
  - <a href="sdk-for-ios-explore-enums-persistentmaprepairerror">PersistentMapRepairError</a>
  - <a href="sdk-for-ios-explore-enums-persistentmapstatus">PersistentMapStatus</a>
  - <a href="sdk-for-ios-explore-structs-region">Region</a>
  - <a href="sdk-for-ios-explore-structs-regionid">RegionId</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk19ServerStartedHandlea">ServerStartedHandle</a>
  - <a href="sdk-for-ios-explore-structs-sslclientcredentialsoptions">SslClientCredentialsOptions</a>
  - <a href="sdk-for-ios-explore-structs-sslservercredentialsoptions">SslServerCredentialsOptions</a>
  - <a href="sdk-for-ios-explore-structs-updatestatistics">UpdateStatistics</a>
- <a href="sdk-for-ios-explore-mapmatcher">MapMatcher</a>
  - <a href="sdk-for-ios-explore-classes-mapmatcher">MapMatcher</a>
  - <a href="sdk-for-ios-explore-structs-matchedlocation">MatchedLocation</a>
- <a href="sdk-for-ios-explore-maps">Maps</a>
  - <a href="sdk-for-ios-explore-protocols-animationdelegate">AnimationDelegate</a>
  - <a href="sdk-for-ios-explore-enums-animationstate">AnimationState</a>
  - <a href="sdk-for-ios-explore-classes-assetsmanager">AssetsManager</a>
  - <a href="sdk-for-ios-explore-classes-dataattributes">DataAttributes</a>
  - <a href="sdk-for-ios-explore-classes-dataattributesaccessor">DataAttributesAccessor</a>
  - <a href="sdk-for-ios-explore-classes-dataattributesbuilder">DataAttributesBuilder</a>
  - <a href="sdk-for-ios-explore-classes-dataattributevalue">DataAttributeValue</a>
  - <a href="sdk-for-ios-explore-classes-dataattributevalue-valuetype">– ValueType</a>
  - <a href="sdk-for-ios-explore-structs-dashpattern">DashPattern</a>
  - <a href="sdk-for-ios-explore-protocols-doubletapdelegate">DoubleTapDelegate</a>
  - <a href="sdk-for-ios-explore-enums-drawordertype">DrawOrderType</a>
  - <a href="sdk-for-ios-explore-classes-easing">Easing</a>
  - <a href="sdk-for-ios-explore-classes-easing-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-enums-easingfunction">EasingFunction</a>
  - <a href="sdk-for-ios-explore-structs-geocoordinateskeyframe">GeoCoordinatesKeyframe</a>
  - <a href="sdk-for-ios-explore-structs-geoorientationkeyframe">GeoOrientationKeyframe</a>
  - <a href="sdk-for-ios-explore-enums-gesturestate">GestureState</a>
  - <a href="sdk-for-ios-explore-enums-gesturetype">GestureType</a>
  - <a href="sdk-for-ios-explore-classes-gestures">Gestures</a>
  - <a href="sdk-for-ios-explore-classes-heremap">HereMap</a>
  - <a href="sdk-for-ios-explore-classes-iconprovider">IconProvider</a>
  - <a href="sdk-for-ios-explore-enums-iconproviderassettype">IconProviderAssetType</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk20IconProviderCallbacka">IconProviderCallback</a>
  - <a href="sdk-for-ios-explore-enums-iconprovidererror">IconProviderError</a>
  - <a href="sdk-for-ios-explore-enums-imageformat">ImageFormat</a>
  - <a href="sdk-for-ios-explore-classes-jsonstylefactory">JsonStyleFactory</a>
  - <a href="sdk-for-ios-explore-classes-jsonstylefactory-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-jsonstylefactory-instantiationerrordetails">– InstantiationErrorDetails</a>
  - <a href="sdk-for-ios-explore-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a>
  - <a href="sdk-for-ios-explore-enums-linecap">LineCap</a>
  - <a href="sdk-for-ios-explore-classes-linetiledatasource">LineTileDataSource</a>
  - <a href="sdk-for-ios-explore-protocols-linetilesource">LineTileSource</a>
  - <a href="sdk-for-ios-explore-protocols-linetilesourceloadresulthandler">LineTileSourceLoadResultHandler</a>
  - <a href="sdk-for-ios-explore-classes-locationindicator">LocationIndicator</a>
  - <a href="sdk-for-ios-explore-classes-locationindicator-indicatorstyle">– IndicatorStyle</a>
  - <a href="sdk-for-ios-explore-classes-locationindicator-markertype">– MarkerType</a>
  - <a href="sdk-for-ios-explore-protocols-longpressdelegate">LongPressDelegate</a>
  - <a href="sdk-for-ios-explore-classes-maparrow">MapArrow</a>
  - <a href="sdk-for-ios-explore-classes-mapcamera">MapCamera</a>
  - <a href="sdk-for-ios-explore-classes-mapcamera-state">– State</a>
  - <a href="sdk-for-ios-explore-classes-mapcamera-farplaneconfiguration">– FarPlaneConfiguration</a>
  - <a href="sdk-for-ios-explore-classes-mapcameraanimation">MapCameraAnimation</a>
  - <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mapcameraanimationfactory">MapCameraAnimationFactory</a>
  - <a href="sdk-for-ios-explore-protocols-mapcameradelegate">MapCameraDelegate</a>
  - <a href="sdk-for-ios-explore-classes-mapcamerakeyframetrack">MapCameraKeyframeTrack</a>
  - <a href="sdk-for-ios-explore-classes-mapcamerakeyframetrack-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mapcameralimits">MapCameraLimits</a>
  - <a href="sdk-for-ios-explore-classes-mapcameraupdate">MapCameraUpdate</a>
  - <a href="sdk-for-ios-explore-classes-mapcameraupdate-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mapcameraupdatefactory">MapCameraUpdateFactory</a>
  - <a href="sdk-for-ios-explore-enums-mapcontentcategory">MapContentCategory</a>
  - <a href="sdk-for-ios-explore-classes-mapcontentsettings">MapContentSettings</a>
  - <a href="sdk-for-ios-explore-classes-mapcontentsettings-trafficrefreshperioderrorcode">– TrafficRefreshPeriodErrorCode</a>
  - <a href="sdk-for-ios-explore-enums-mapcontenttype">MapContentType</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext">MapContext</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementstrategy">– MemoryManagementStrategy</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementresultcode">– MemoryManagementResultCode</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-resourcetype">– ResourceType</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-freeresourceseverity">– FreeResourceSeverity</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementresult">– MemoryManagementResult</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementoptions">– MemoryManagementOptions</a>
  - <a href="sdk-for-ios-explore-enums-maperror">MapError</a>
  - <a href="sdk-for-ios-explore-structs-mapfeatures">MapFeatures</a>
  - <a href="sdk-for-ios-explore-structs-mapfeaturemodes">MapFeatureModes</a>
  - <a href="sdk-for-ios-explore-protocols-mapidledelegate">MapIdleDelegate</a>
  - <a href="sdk-for-ios-explore-classes-mapimage">MapImage</a>
  - <a href="sdk-for-ios-explore-classes-mapimageoverlay">MapImageOverlay</a>
  - <a href="sdk-for-ios-explore-classes-mapitemkeyframetrack">MapItemKeyFrameTrack</a>
  - <a href="sdk-for-ios-explore-classes-mapitemkeyframetrack-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk21MapItemRepresentationC">MapItemRepresentation</a>
  - <a href="sdk-for-ios-explore-classes-maplayer">MapLayer</a>
  - <a href="sdk-for-ios-explore-classes-maplayerbuilder">MapLayerBuilder</a>
  - <a href="sdk-for-ios-explore-classes-maplayerbuilder-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-maplayerbuilder-instantiationerrordetails">– InstantiationErrorDetails</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk16MapLayerPriorityC">MapLayerPriority</a>
  - <a href="sdk-for-ios-explore-classes-maplayerprioritybuilder">MapLayerPriorityBuilder</a>
  - <a href="sdk-for-ios-explore-classes-maplayermapmeasuredependentstoragelevels">MapLayerMapMeasureDependentStorageLevels</a>
  - <a href="sdk-for-ios-explore-structs-maplayervisibilityrange">MapLayerVisibilityRange</a>
  - <a href="sdk-for-ios-explore-classes-mapmarkercluster">MapMarkerCluster</a>
  - <a href="sdk-for-ios-explore-classes-mapmarkercluster-grouping">– Grouping</a>
  - <a href="sdk-for-ios-explore-classes-mapmarkercluster-imagestyle">– ImageStyle</a>
  - <a href="sdk-for-ios-explore-classes-mapmarkercluster-counterstyle">– CounterStyle</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasurerange">MapMeasureRange</a>
  - <a href="sdk-for-ios-explore-classes-mapobjectdescriptor">MapObjectDescriptor</a>
  - <a href="sdk-for-ios-explore-enums-mapprojection">MapProjection</a>
  - <a href="sdk-for-ios-explore-classes-mapscenelights">MapSceneLights</a>
  - <a href="sdk-for-ios-explore-classes-mapscenelights-category">– Category</a>
  - <a href="sdk-for-ios-explore-classes-mapscenelights-attributesettingerror">– AttributeSettingError</a>
  - <a href="sdk-for-ios-explore-classes-mapscenelights-direction">– Direction</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk19MapSceneLoadOptionsC">MapSceneLoadOptions</a>
  - <a href="sdk-for-ios-explore-classes-mapsceneloadoptionsbuilder">MapSceneLoadOptionsBuilder</a>
  - <a href="sdk-for-ios-explore-classes-mapsceneloadoptionsbuilder-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mapsceneloadoptionsbuilder-instantiationerrordetails">– InstantiationErrorDetails</a>
  - <a href="sdk-for-ios-explore-classes-mapmarker">MapMarker</a>
  - <a href="sdk-for-ios-explore-classes-mapmarker-textstyle">– TextStyle</a>
  - <a href="sdk-for-ios-explore-classes-mapmarker3d">MapMarker3D</a>
  - <a href="sdk-for-ios-explore-classes-mapmarker3dmodel">MapMarker3DModel</a>
  - <a href="sdk-for-ios-explore-classes-mapmarker3dmodel-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mapmarkeranimation">MapMarkerAnimation</a>
  - <a href="sdk-for-ios-explore-classes-mapmarkeranimation-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasure">MapMeasure</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasure-kind">– Kind</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mappolygon">MapPolygon</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline">MapPolyline</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-representation">– Representation</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation">– DashImageRepresentation</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-solidrepresentation">– SolidRepresentation</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation">– DashRepresentation</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-solidmulticolorrepresentation">– SolidMultiColorRepresentation</a>
  - <a href="sdk-for-ios-explore-classes-mappolylineanimation">MapPolylineAnimation</a>
  - <a href="sdk-for-ios-explore-classes-mappolylineanimation-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mappickresult">MapPickResult</a>
  - <a href="sdk-for-ios-explore-classes-mapscene">MapScene</a>
  - <a href="sdk-for-ios-explore-classes-mapscene-mappickfilter">– MapPickFilter</a>
  - <a href="sdk-for-ios-explore-enums-mapscheme">MapScheme</a>
  - <a href="sdk-for-ios-explore-protocols-mapviewbase">MapViewBase</a>
  - <a href="sdk-for-ios-explore-classes-mapview">MapView</a>
  - <a href="sdk-for-ios-explore-classes-mapview-viewpin">– ViewPin</a>
  - <a href="sdk-for-ios-explore-protocols-mapviewlifecycledelegate">MapViewLifecycleDelegate</a>
  - <a href="sdk-for-ios-explore-structs-mapviewoptions">MapViewOptions</a>
  - <a href="sdk-for-ios-explore-structs-materialreflectivity">MaterialReflectivity</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk4MeshC">Mesh</a>
  - <a href="sdk-for-ios-explore-classes-meshbuilder">MeshBuilder</a>
  - <a href="sdk-for-ios-explore-protocols-pandelegate">PanDelegate</a>
  - <a href="sdk-for-ios-explore-classes-pickmapcontentresult">PickMapContentResult</a>
  - <a href="sdk-for-ios-explore-classes-pickmapcontentresult-trafficincidentresult">– TrafficIncidentResult</a>
  - <a href="sdk-for-ios-explore-classes-pickmapcontentresult-vehiclerestrictionresult">– VehicleRestrictionResult</a>
  - <a href="sdk-for-ios-explore-classes-pickmapitemsresult">PickMapItemsResult</a>
  - <a href="sdk-for-ios-explore-protocols-pinchrotatedelegate">PinchRotateDelegate</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk9PointDataC">PointData</a>
  - <a href="sdk-for-ios-explore-classes-pointdataaccessor">PointDataAccessor</a>
  - <a href="sdk-for-ios-explore-classes-pointdatabuilder">PointDataBuilder</a>
  - <a href="sdk-for-ios-explore-classes-pointdatasource">PointDataSource</a>
  - <a href="sdk-for-ios-explore-classes-pointdatasourcebuilder">PointDataSourceBuilder</a>
  - <a href="sdk-for-ios-explore-classes-pointtiledatasource">PointTileDataSource</a>
  - <a href="sdk-for-ios-explore-protocols-pointtilesource">PointTileSource</a>
  - <a href="sdk-for-ios-explore-protocols-pointtilesourceloadresulthandler">PointTileSourceLoadResultHandler</a>
  - <a href="sdk-for-ios-explore-structs-point2dkeyframe">Point2DKeyframe</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk11PolygonDataC">PolygonData</a>
  - <a href="sdk-for-ios-explore-classes-polygondataaccessor">PolygonDataAccessor</a>
  - <a href="sdk-for-ios-explore-classes-polygondatabuilder">PolygonDataBuilder</a>
  - <a href="sdk-for-ios-explore-classes-polygondatasource">PolygonDataSource</a>
  - <a href="sdk-for-ios-explore-classes-polygondatasourcebuilder">PolygonDataSourceBuilder</a>
  - <a href="sdk-for-ios-explore-classes-polygontiledatasource">PolygonTileDataSource</a>
  - <a href="sdk-for-ios-explore-protocols-polygontilesource">PolygonTileSource</a>
  - <a href="sdk-for-ios-explore-protocols-polygontilesourceloadresulthandler">PolygonTileSourceLoadResultHandler</a>
  - <a href="sdk-for-ios-explore-classes-quadmeshbuilder">QuadMeshBuilder</a>
  - <a href="sdk-for-ios-explore-classes-rasterdatasource">RasterDataSource</a>
  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration">RasterDataSourceConfiguration</a>
  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration-provider">– Provider</a>
  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration-cache">– Cache</a>
  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfigurationupdate">RasterDataSourceConfigurationUpdate</a>
  - <a href="sdk-for-ios-explore-protocols-rasterdatasourcedelegate">RasterDataSourceDelegate</a>
  - <a href="sdk-for-ios-explore-enums-rasterdatasourceerror">RasterDataSourceError</a>
  - <a href="sdk-for-ios-explore-protocols-rastertilesource">RasterTileSource</a>
  - <a href="sdk-for-ios-explore-protocols-rastertilesourceloadresulthandler">RasterTileSourceLoadResultHandler</a>
  - <a href="sdk-for-ios-explore-structs-roadshieldiconproperties">RoadShieldIconProperties</a>
  - <a href="sdk-for-ios-explore-structs-rendersize">RenderSize</a>
  - <a href="sdk-for-ios-explore-structs-rendersize-unit">– Unit</a>
  - <a href="sdk-for-ios-explore-structs-scalarkeyframe">ScalarKeyframe</a>
  - <a href="sdk-for-ios-explore-classes-sdkmapviewinitializer">SDKMapViewInitializer</a>
  - <a href="sdk-for-ios-explore-enums-shadowquality">ShadowQuality</a>
  - <a href="sdk-for-ios-explore-classes-style">Style</a>
  - <a href="sdk-for-ios-explore-protocols-tapdelegate">TapDelegate</a>
  - <a href="sdk-for-ios-explore-classes-tilegeoboundscalculator">TileGeoBoundsCalculator</a>
  - <a href="sdk-for-ios-explore-protocols-tilesource">TileSource</a>
  - <a href="sdk-for-ios-explore-structs-tilesourcedataversion">TileSourceDataVersion</a>
  - <a href="sdk-for-ios-explore-protocols-tilesourcedelegate">TileSourceDelegate</a>
  - <a href="sdk-for-ios-explore-protocols-tilesourceloadtilerequesthandle">TileSourceLoadTileRequestHandle</a>
  - <a href="sdk-for-ios-explore-structs-tilesourcetilemetadata">TileSourceTileMetadata</a>
  - <a href="sdk-for-ios-explore-structs-tilekey">TileKey</a>
  - <a href="sdk-for-ios-explore-classes-tileurlproviderfactory">TileUrlProviderFactory</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk21TileUrlRequestHandlera">TileUrlRequestHandler</a>
  - <a href="sdk-for-ios-explore-enums-tilingscheme">TilingScheme</a>
  - <a href="sdk-for-ios-explore-classes-translucentmaplayergroup">TranslucentMapLayerGroup</a>
  - <a href="sdk-for-ios-explore-classes-translucentmaplayergroup-errorcode">– ErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-translucentmaplayergroup-errordetails">– ErrorDetails</a>
  - <a href="sdk-for-ios-explore-classes-trianglemeshbuilder">TriangleMeshBuilder</a>
  - <a href="sdk-for-ios-explore-protocols-twofingerpandelegate">TwoFingerPanDelegate</a>
  - <a href="sdk-for-ios-explore-protocols-twofingertapdelegate">TwoFingerTapDelegate</a>
  - <a href="sdk-for-ios-explore-enums-visibilitystate">VisibilityState</a>
  - <a href="sdk-for-ios-explore-structs-vehiclerestrictioniconproperties">VehicleRestrictionIconProperties</a>
  - <a href="sdk-for-ios-explore-enums-watermarkstyle">WatermarkStyle</a>
- <a href="sdk-for-ios-explore-routing">Routing</a>
  - <a href="sdk-for-ios-explore-enums-accessattributes">AccessAttributes</a>
  - <a href="sdk-for-ios-explore-structs-agency">Agency</a>
  - <a href="sdk-for-ios-explore-structs-allowoptions">AllowOptions</a>
  - <a href="sdk-for-ios-explore-structs-attribution">Attribution</a>
  - <a href="sdk-for-ios-explore-enums-attributiontype">AttributionType</a>
  - <a href="sdk-for-ios-explore-structs-avoidanceoptions">AvoidanceOptions</a>
  - <a href="sdk-for-ios-explore-structs-avoidboundingboxareaoptions">AvoidBoundingBoxAreaOptions</a>
  - <a href="sdk-for-ios-explore-structs-avoidcorridorareaoptions">AvoidCorridorAreaOptions</a>
  - <a href="sdk-for-ios-explore-structs-avoidpolygonareaoptions">AvoidPolygonAreaOptions</a>
  - <a href="sdk-for-ios-explore-structs-batteryspecifications">BatterySpecifications</a>
  - <a href="sdk-for-ios-explore-structs-bicycleoptions">BicycleOptions</a>
  - <a href="sdk-for-ios-explore-structs-busoptions">BusOptions</a>
  - <a href="sdk-for-ios-explore-structs-caroptions">CarOptions</a>
  - <a href="sdk-for-ios-explore-routing#/s:7heresdk37CalculateIndoorRouteCompletionHandlera">CalculateIndoorRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-routing#/s:7heresdk33CalculateIsolineCompletionHandlera">CalculateIsolineCompletionHandler</a>
  - <a href="sdk-for-ios-explore-routing#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-routing#/s:7heresdk40CalculateTrafficOnRouteCompletionHandlera">CalculateTrafficOnRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-structs-chargingactiondetails">ChargingActionDetails</a>
  - <a href="sdk-for-ios-explore-structs-chargingconnectorattributes">ChargingConnectorAttributes</a>
  - <a href="sdk-for-ios-explore-enums-chargingconnectortype">ChargingConnectorType</a>
  - <a href="sdk-for-ios-explore-enums-chargingconnectortype-key">– Key</a>
  - <a href="sdk-for-ios-explore-enums-chargingconnectortype-codingerror">– CodingError</a>
  - <a href="sdk-for-ios-explore-structs-chargingstation">ChargingStation</a>
  - <a href="sdk-for-ios-explore-structs-chargingstop">ChargingStop</a>
  - <a href="sdk-for-ios-explore-enums-chargingsupplytype">ChargingSupplyType</a>
  - <a href="sdk-for-ios-explore-structs-dynamicspeedinfo">DynamicSpeedInfo</a>
  - <a href="sdk-for-ios-explore-structs-electricvehicleoptions">ElectricVehicleOptions</a>
  - <a href="sdk-for-ios-explore-structs-empiricalconsumptionmodel">EmpiricalConsumptionModel</a>
  - <a href="sdk-for-ios-explore-structs-evcaroptions">EVCarOptions</a>
  - <a href="sdk-for-ios-explore-structs-evchargingpool">EVChargingPool</a>
  - <a href="sdk-for-ios-explore-structs-evchargingstation">EVChargingStation</a>
  - <a href="sdk-for-ios-explore-structs-evconsumptionmodel">EVConsumptionModel</a>
  - <a href="sdk-for-ios-explore-structs-evmobilityserviceproviderpreferences">EVMobilityServiceProviderPreferences</a>
  - <a href="sdk-for-ios-explore-structs-evtruckoptions">EVTruckOptions</a>
  - <a href="sdk-for-ios-explore-structs-fare">Fare</a>
  - <a href="sdk-for-ios-explore-structs-farepassvalidityperiod">FarePassValidityPeriod</a>
  - <a href="sdk-for-ios-explore-enums-farepassvalidityperiodtype">FarePassValidityPeriodType</a>
  - <a href="sdk-for-ios-explore-structs-fareprice">FarePrice</a>
  - <a href="sdk-for-ios-explore-enums-farepricetype">FarePriceType</a>
  - <a href="sdk-for-ios-explore-enums-farereason">FareReason</a>
  - <a href="sdk-for-ios-explore-enums-functionalroadclass">FunctionalRoadClass</a>
  - <a href="sdk-for-ios-explore-enums-hazardousmaterial">HazardousMaterial</a>
  - <a href="sdk-for-ios-explore-structs-indooravoidanceoptions">IndoorAvoidanceOptions</a>
  - <a href="sdk-for-ios-explore-classes-indoormaneuver">IndoorManeuver</a>
  - <a href="sdk-for-ios-explore-structs-indoorrouteoptions">IndoorRouteOptions</a>
  - <a href="sdk-for-ios-explore-classes-indoorroutestyle">IndoorRouteStyle</a>
  - <a href="sdk-for-ios-explore-classes-indoorroutingcontroller">IndoorRoutingController</a>
  - <a href="sdk-for-ios-explore-classes-indoorroutingengine">IndoorRoutingEngine</a>
  - <a href="sdk-for-ios-explore-enums-indoorroutingerror">IndoorRoutingError</a>
  - <a href="sdk-for-ios-explore-classes-indoorwaypoint">IndoorWaypoint</a>
  - <a href="sdk-for-ios-explore-classes-isoline">Isoline</a>
  - <a href="sdk-for-ios-explore-enums-isolinecalculationmode">IsolineCalculationMode</a>
  - <a href="sdk-for-ios-explore-structs-isolineoptions">IsolineOptions</a>
  - <a href="sdk-for-ios-explore-structs-isolineoptions-calculation">– Calculation</a>
  - <a href="sdk-for-ios-explore-enums-isolinerangetype">IsolineRangeType</a>
  - <a href="sdk-for-ios-explore-classes-isolineroutingengine">IsolineRoutingEngine</a>
  - <a href="sdk-for-ios-explore-enums-localizedtextpreference">LocalizedTextPreference</a>
  - <a href="sdk-for-ios-explore-classes-maneuver">Maneuver</a>
  - <a href="sdk-for-ios-explore-enums-maneuveraction">ManeuverAction</a>
  - <a href="sdk-for-ios-explore-structs-mapdatasize">MapDataSize</a>
  - <a href="sdk-for-ios-explore-protocols-mapdatasizelistener">MapDataSizeListener</a>
  - <a href="sdk-for-ios-explore-structs-mapmatchedcoordinates">MapMatchedCoordinates</a>
  - <a href="sdk-for-ios-explore-enums-matchsideofstreet">MatchSideOfStreet</a>
  - <a href="sdk-for-ios-explore-structs-maxaxlegroupweight">MaxAxleGroupWeight</a>
  - <a href="sdk-for-ios-explore-structs-maxspeedonsegment">MaxSpeedOnSegment</a>
  - <a href="sdk-for-ios-explore-enums-noticeseverity">NoticeSeverity</a>
  - <a href="sdk-for-ios-explore-classes-offlineroutingengine">OfflineRoutingEngine</a>
  - <a href="sdk-for-ios-explore-structs-offlineroutingengineoptions">OfflineRoutingEngineOptions</a>
  - <a href="sdk-for-ios-explore-enums-optimizationmode">OptimizationMode</a>
  - <a href="sdk-for-ios-explore-structs-passthroughwaypoint">PassThroughWaypoint</a>
  - <a href="sdk-for-ios-explore-enums-paymentmethod">PaymentMethod</a>
  - <a href="sdk-for-ios-explore-structs-pedestrianoptions">PedestrianOptions</a>
  - <a href="sdk-for-ios-explore-structs-physicalconsumptionmodel">PhysicalConsumptionModel</a>
  - <a href="sdk-for-ios-explore-classes-polygonprefetcher">PolygonPrefetcher</a>
  - <a href="sdk-for-ios-explore-structs-postaction">PostAction</a>
  - <a href="sdk-for-ios-explore-protocols-postactiondelegate">PostActionDelegate</a>
  - <a href="sdk-for-ios-explore-enums-postactiontype">PostActionType</a>
  - <a href="sdk-for-ios-explore-structs-preaction">PreAction</a>
  - <a href="sdk-for-ios-explore-enums-preactiontype">PreActionType</a>
  - <a href="sdk-for-ios-explore-protocols-prefetchstatuslistener">PrefetchStatusListener</a>
  - <a href="sdk-for-ios-explore-structs-privatebusoptions">PrivateBusOptions</a>
  - <a href="sdk-for-ios-explore-classes-refreshrouteoptions">RefreshRouteOptions</a>
  - <a href="sdk-for-ios-explore-structs-roadattributes">RoadAttributes</a>
  - <a href="sdk-for-ios-explore-protocols-roadattributesdelegate">RoadAttributesDelegate</a>
  - <a href="sdk-for-ios-explore-enums-roadfeatures">RoadFeatures</a>
  - <a href="sdk-for-ios-explore-structs-roadtexts">RoadTexts</a>
  - <a href="sdk-for-ios-explore-classes-route">Route</a>
  - <a href="sdk-for-ios-explore-structs-routehandle">RouteHandle</a>
  - <a href="sdk-for-ios-explore-structs-routelabel">RouteLabel</a>
  - <a href="sdk-for-ios-explore-enums-routelabeltype">RouteLabelType</a>
  - <a href="sdk-for-ios-explore-structs-routeoffset">RouteOffset</a>
  - <a href="sdk-for-ios-explore-structs-routeoptions">RouteOptions</a>
  - <a href="sdk-for-ios-explore-structs-routeplace">RoutePlace</a>
  - <a href="sdk-for-ios-explore-enums-routeplacedirection">RoutePlaceDirection</a>
  - <a href="sdk-for-ios-explore-enums-routeplacetype">RoutePlaceType</a>
  - <a href="sdk-for-ios-explore-classes-routeprefetcher">RoutePrefetcher</a>
  - <a href="sdk-for-ios-explore-structs-routerailwaycrossing">RouteRailwayCrossing</a>
  - <a href="sdk-for-ios-explore-enums-routerailwaycrossingtype">RouteRailwayCrossingType</a>
  - <a href="sdk-for-ios-explore-structs-routestop">RouteStop</a>
  - <a href="sdk-for-ios-explore-structs-routetextoptions">RouteTextOptions</a>
  - <a href="sdk-for-ios-explore-structs-routingconnectionsettings">RoutingConnectionSettings</a>
  - <a href="sdk-for-ios-explore-classes-routingengine">RoutingEngine</a>
  - <a href="sdk-for-ios-explore-enums-routingerror">RoutingError</a>
  - <a href="sdk-for-ios-explore-structs-routingoptions">RoutingOptions</a>
  - <a href="sdk-for-ios-explore-protocols-routingprotocol">RoutingProtocol</a>
  - <a href="sdk-for-ios-explore-structs-scooteroptions">ScooterOptions</a>
  - <a href="sdk-for-ios-explore-classes-section">Section</a>
  - <a href="sdk-for-ios-explore-structs-sectionnotice">SectionNotice</a>
  - <a href="sdk-for-ios-explore-enums-sectionnoticecode">SectionNoticeCode</a>
  - <a href="sdk-for-ios-explore-enums-sectiontransportmode">SectionTransportMode</a>
  - <a href="sdk-for-ios-explore-structs-segmentreference">SegmentReference</a>
  - <a href="sdk-for-ios-explore-enums-sideofdestination">SideOfDestination</a>
  - <a href="sdk-for-ios-explore-structs-signpost">Signpost</a>
  - <a href="sdk-for-ios-explore-structs-signpostlabel">SignpostLabel</a>
  - <a href="sdk-for-ios-explore-enums-streetattributes">StreetAttributes</a>
  - <a href="sdk-for-ios-explore-classes-span">Span</a>
  - <a href="sdk-for-ios-explore-structs-taxioptions">TaxiOptions</a>
  - <a href="sdk-for-ios-explore-structs-textusageoptions">TextUsageOptions</a>
  - <a href="sdk-for-ios-explore-structs-toll">Toll</a>
  - <a href="sdk-for-ios-explore-structs-tollfare">TollFare</a>
  - <a href="sdk-for-ios-explore-structs-tollfarepass">TollFarePass</a>
  - <a href="sdk-for-ios-explore-structs-tolloptions">TollOptions</a>
  - <a href="sdk-for-ios-explore-structs-tolloptions-vehiclecategory">– VehicleCategory</a>
  - <a href="sdk-for-ios-explore-structs-tolloptions-emissiontype">– EmissionType</a>
  - <a href="sdk-for-ios-explore-structs-trafficonroute">TrafficOnRoute</a>
  - <a href="sdk-for-ios-explore-structs-trafficonspan">TrafficOnSpan</a>
  - <a href="sdk-for-ios-explore-structs-trafficonsection">TrafficOnSection</a>
  - <a href="sdk-for-ios-explore-structs-transitdeparture">TransitDeparture</a>
  - <a href="sdk-for-ios-explore-enums-transitdeparturestatus">TransitDepartureStatus</a>
  - <a href="sdk-for-ios-explore-structs-transitincident">TransitIncident</a>
  - <a href="sdk-for-ios-explore-enums-transitincidenteffect">TransitIncidentEffect</a>
  - <a href="sdk-for-ios-explore-enums-transitincidenttype">TransitIncidentType</a>
  - <a href="sdk-for-ios-explore-enums-transitmode">TransitMode</a>
  - <a href="sdk-for-ios-explore-enums-transitmodefilter">TransitModeFilter</a>
  - <a href="sdk-for-ios-explore-enums-trafficoptimizationmode">TrafficOptimizationMode</a>
  - <a href="sdk-for-ios-explore-structs-transitrouteoptions">TransitRouteOptions</a>
  - <a href="sdk-for-ios-explore-classes-transitroutingengine">TransitRoutingEngine</a>
  - <a href="sdk-for-ios-explore-structs-transitsectiondetails">TransitSectionDetails</a>
  - <a href="sdk-for-ios-explore-structs-transitstop">TransitStop</a>
  - <a href="sdk-for-ios-explore-structs-transittransport">TransitTransport</a>
  - <a href="sdk-for-ios-explore-structs-transitwaypoint">TransitWaypoint</a>
  - <a href="sdk-for-ios-explore-enums-traveldirection">TravelDirection</a>
  - <a href="sdk-for-ios-explore-structs-truckoptions">TruckOptions</a>
  - <a href="sdk-for-ios-explore-structs-truckspecifications">TruckSpecifications</a>
  - <a href="sdk-for-ios-explore-enums-trucktype">TruckType</a>
  - <a href="sdk-for-ios-explore-enums-tunnelcategory">TunnelCategory</a>
  - <a href="sdk-for-ios-explore-structs-vehiclerestrictionmaxweight">VehicleRestrictionMaxWeight</a>
  - <a href="sdk-for-ios-explore-enums-vehiclerestrictionmaxweighttype">VehicleRestrictionMaxWeightType</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification">VehicleSpecification</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification-carbuilder">– CarBuilder</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification-truckbuilder">– TruckBuilder</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification-scooterbuilder">– ScooterBuilder</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification-taxibuilder">– TaxiBuilder</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification-busbuilder">– BusBuilder</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification-privatebusbuilder">– PrivateBusBuilder</a>
  - <a href="sdk-for-ios-explore-structs-violatedrestriction">ViolatedRestriction</a>
  - <a href="sdk-for-ios-explore-structs-violatedrestriction-details">– Details</a>
  - <a href="sdk-for-ios-explore-enums-walkattributes">WalkAttributes</a>
  - <a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a>
  - <a href="sdk-for-ios-explore-enums-waypointtype">WaypointType</a>
  - <a href="sdk-for-ios-explore-enums-zonecategory">ZoneCategory</a>
- <a href="sdk-for-ios-explore-navigation">Navigation</a>
  - <a href="sdk-for-ios-explore-classes-areacamerabehavior">AreaCameraBehavior</a>
  - <a href="sdk-for-ios-explore-enums-arrivalnotificationoption">ArrivalNotificationOption</a>
  - <a href="sdk-for-ios-explore-enums-aspectratio">AspectRatio</a>
  - <a href="sdk-for-ios-explore-classes-automotivecamerabehavior">AutomotiveCameraBehavior</a>
  - <a href="sdk-for-ios-explore-classes-automotivecamerabehavior-orientationmode">– OrientationMode</a>
  - <a href="sdk-for-ios-explore-classes-automotivecamerabehavior-activecameratype">– ActiveCameraType</a>
  - <a href="sdk-for-ios-explore-enums-bordercrossingtype">BorderCrossingType</a>
  - <a href="sdk-for-ios-explore-structs-bordercrossingwarning">BorderCrossingWarning</a>
  - <a href="sdk-for-ios-explore-protocols-bordercrossingwarningdelegate">BorderCrossingWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-bordercrossingwarningoptions">BorderCrossingWarningOptions</a>
  - <a href="sdk-for-ios-explore-protocols-camerabehavior">CameraBehavior</a>
  - <a href="sdk-for-ios-explore-structs-currentsituationlaneview">CurrentSituationLaneView</a>
  - <a href="sdk-for-ios-explore-structs-currentsituationlaneassistanceview">CurrentSituationLaneAssistanceView</a>
  - <a href="sdk-for-ios-explore-protocols-currentsituationlaneassistanceviewdelegate">CurrentSituationLaneAssistanceViewDelegate</a>
  - <a href="sdk-for-ios-explore-structs-custompanningdata">CustomPanningData</a>
  - <a href="sdk-for-ios-explore-structs-dangerzonewarning">DangerZoneWarning</a>
  - <a href="sdk-for-ios-explore-protocols-dangerzonewarningdelegate">DangerZoneWarningDelegate</a>
  - <a href="sdk-for-ios-explore-protocols-destinationreacheddelegate">DestinationReachedDelegate</a>
  - <a href="sdk-for-ios-explore-structs-dimensionrestriction">DimensionRestriction</a>
  - <a href="sdk-for-ios-explore-enums-dimensionrestrictiontype">DimensionRestrictionType</a>
  - <a href="sdk-for-ios-explore-enums-directioninformationusageoption">DirectionInformationUsageOption</a>
  - <a href="sdk-for-ios-explore-enums-distancetype">DistanceType</a>
  - <a href="sdk-for-ios-explore-enums-dividermarker">DividerMarker</a>
  - <a href="sdk-for-ios-explore-classes-dynamiccamerabehavior">DynamicCameraBehavior</a>
  - <a href="sdk-for-ios-explore-classes-dynamicroutingengine">DynamicRoutingEngine</a>
  - <a href="sdk-for-ios-explore-classes-dynamicroutingengine-starterror">– StartError</a>
  - <a href="sdk-for-ios-explore-protocols-dynamicroutingdelegate">DynamicRoutingDelegate</a>
  - <a href="sdk-for-ios-explore-structs-dynamicroutingengineoptions">DynamicRoutingEngineOptions</a>
  - <a href="sdk-for-ios-explore-structs-environmentalzonewarning">EnvironmentalZoneWarning</a>
  - <a href="sdk-for-ios-explore-protocols-environmentalzonewarningdelegate">EnvironmentalZoneWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-eventtext">EventText</a>
  - <a href="sdk-for-ios-explore-protocols-eventtextdelegate">EventTextDelegate</a>
  - <a href="sdk-for-ios-explore-structs-eventtextoptions">EventTextOptions</a>
  - <a href="sdk-for-ios-explore-classes-fixedcamerabehavior">FixedCameraBehavior</a>
  - <a href="sdk-for-ios-explore-enums-generalwarningroadsigntype">GeneralWarningRoadSignType</a>
  - <a href="sdk-for-ios-explore-classes-gpxdocument">GPXDocument</a>
  - <a href="sdk-for-ios-explore-structs-gpxoptions">GPXOptions</a>
  - <a href="sdk-for-ios-explore-classes-gpxtrack">GPXTrack</a>
  - <a href="sdk-for-ios-explore-classes-gpxtrackwriter">GPXTrackWriter</a>
  - <a href="sdk-for-ios-explore-protocols-interpolatedlocationdelegate">InterpolatedLocationDelegate</a>
  - <a href="sdk-for-ios-explore-structs-junctionviewlaneassistance">JunctionViewLaneAssistance</a>
  - <a href="sdk-for-ios-explore-protocols-junctionviewlaneassistancedelegate">JunctionViewLaneAssistanceDelegate</a>
  - <a href="sdk-for-ios-explore-structs-lane">Lane</a>
  - <a href="sdk-for-ios-explore-structs-laneaccess">LaneAccess</a>
  - <a href="sdk-for-ios-explore-enums-lanedirection">LaneDirection</a>
  - <a href="sdk-for-ios-explore-structs-lanedirectioncategory">LaneDirectionCategory</a>
  - <a href="sdk-for-ios-explore-structs-lanemarkings">LaneMarkings</a>
  - <a href="sdk-for-ios-explore-enums-lanerecommendationstate">LaneRecommendationState</a>
  - <a href="sdk-for-ios-explore-structs-lanetype">LaneType</a>
  - <a href="sdk-for-ios-explore-structs-lowspeedzonewarning">LowSpeedZoneWarning</a>
  - <a href="sdk-for-ios-explore-protocols-lowspeedzonewarningdelegate">LowSpeedZoneWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-maneuvernotificationdetails">ManeuverNotificationDetails</a>
  - <a href="sdk-for-ios-explore-structs-maneuvernotificationoptions">ManeuverNotificationOptions</a>
  - <a href="sdk-for-ios-explore-structs-maneuvernotificationtimingoptions">ManeuverNotificationTimingOptions</a>
  - <a href="sdk-for-ios-explore-enums-maneuvernotificationtype">ManeuverNotificationType</a>
  - <a href="sdk-for-ios-explore-structs-maneuverprogress">ManeuverProgress</a>
  - <a href="sdk-for-ios-explore-structs-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a>
  - <a href="sdk-for-ios-explore-protocols-maneuverviewlaneassistancedelegate">ManeuverViewLaneAssistanceDelegate</a>
  - <a href="sdk-for-ios-explore-structs-mapmatchedlocation">MapMatchedLocation</a>
  - <a href="sdk-for-ios-explore-structs-milestone">Milestone</a>
  - <a href="sdk-for-ios-explore-enums-milestonestatus">MilestoneStatus</a>
  - <a href="sdk-for-ios-explore-protocols-milestonestatusdelegate">MilestoneStatusDelegate</a>
  - <a href="sdk-for-ios-explore-enums-milestonetype">MilestoneType</a>
  - <a href="sdk-for-ios-explore-enums-naturalguidancetype">NaturalGuidanceType</a>
  - <a href="sdk-for-ios-explore-structs-navigablelocation">NavigableLocation</a>
  - <a href="sdk-for-ios-explore-protocols-navigablelocationdelegate">NavigableLocationDelegate</a>
  - <a href="sdk-for-ios-explore-classes-navigator">Navigator</a>
  - <a href="sdk-for-ios-explore-protocols-navigatorprotocol">NavigatorProtocol</a>
  - <a href="sdk-for-ios-explore-enums-notificationformatoption">NotificationFormatOption</a>
  - <a href="sdk-for-ios-explore-protocols-offroaddestinationreacheddelegate">OffRoadDestinationReachedDelegate</a>
  - <a href="sdk-for-ios-explore-structs-offroadprogress">OffRoadProgress</a>
  - <a href="sdk-for-ios-explore-protocols-offroadprogressdelegate">OffRoadProgressDelegate</a>
  - <a href="sdk-for-ios-explore-structs-realisticviewrasterimage">RealisticViewRasterImage</a>
  - <a href="sdk-for-ios-explore-structs-realisticviewvectorimage">RealisticViewVectorImage</a>
  - <a href="sdk-for-ios-explore-structs-realisticviewwarning">RealisticViewWarning</a>
  - <a href="sdk-for-ios-explore-protocols-realisticviewwarningdelegate">RealisticViewWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-realisticviewwarningoptions">RealisticViewWarningOptions</a>
  - <a href="sdk-for-ios-explore-structs-railwaycrossingwarning">RailwayCrossingWarning</a>
  - <a href="sdk-for-ios-explore-protocols-railwaycrossingwarningdelegate">RailwayCrossingWarningDelegate</a>
  - <a href="sdk-for-ios-explore-enums-roadclassification">RoadClassification</a>
  - <a href="sdk-for-ios-explore-structs-roadsign">RoadSign</a>
  - <a href="sdk-for-ios-explore-enums-roadsigncategory">RoadSignCategory</a>
  - <a href="sdk-for-ios-explore-enums-roadsigntype">RoadSignType</a>
  - <a href="sdk-for-ios-explore-structs-roadsignwarning">RoadSignWarning</a>
  - <a href="sdk-for-ios-explore-protocols-roadsignwarningdelegate">RoadSignWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-roadsignwarningoptions">RoadSignWarningOptions</a>
  - <a href="sdk-for-ios-explore-enums-roadsignvehicletype">RoadSignVehicleType</a>
  - <a href="sdk-for-ios-explore-protocols-roadtextsdelegate">RoadTextsDelegate</a>
  - <a href="sdk-for-ios-explore-structs-routedeviation">RouteDeviation</a>
  - <a href="sdk-for-ios-explore-protocols-routedeviationdelegate">RouteDeviationDelegate</a>
  - <a href="sdk-for-ios-explore-structs-routematchedlocation">RouteMatchedLocation</a>
  - <a href="sdk-for-ios-explore-structs-routeprogress">RouteProgress</a>
  - <a href="sdk-for-ios-explore-structs-routeprogresscolors">RouteProgressColors</a>
  - <a href="sdk-for-ios-explore-protocols-routeprogressdelegate">RouteProgressDelegate</a>
  - <a href="sdk-for-ios-explore-enums-safetycameratype">SafetyCameraType</a>
  - <a href="sdk-for-ios-explore-structs-safetycamerawarning">SafetyCameraWarning</a>
  - <a href="sdk-for-ios-explore-protocols-safetycamerawarningdelegate">SafetyCameraWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-safetycamerawarningoptions">SafetyCameraWarningOptions</a>
  - <a href="sdk-for-ios-explore-structs-schoolzonewarning">SchoolZoneWarning</a>
  - <a href="sdk-for-ios-explore-protocols-schoolzonewarningdelegate">SchoolZoneWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-schoolzonewarningoptions">SchoolZoneWarningOptions</a>
  - <a href="sdk-for-ios-explore-classes-sdknavigationinitializer">SDKNavigationInitializer</a>
  - <a href="sdk-for-ios-explore-structs-sectionprogress">SectionProgress</a>
  - <a href="sdk-for-ios-explore-classes-spatialaudiocuepanning">SpatialAudioCuePanning</a>
  - <a href="sdk-for-ios-explore-structs-spatialnotificationdetails">SpatialNotificationDetails</a>
  - <a href="sdk-for-ios-explore-structs-spatialtrajectorydata">SpatialTrajectoryData</a>
  - <a href="sdk-for-ios-explore-classes-speedbasedcamerabehavior">SpeedBasedCameraBehavior</a>
  - <a href="sdk-for-ios-explore-classes-speedbasedcamerabehavior-profilevalue">– ProfileValue</a>
  - <a href="sdk-for-ios-explore-structs-speedlimit">SpeedLimit</a>
  - <a href="sdk-for-ios-explore-protocols-speedlimitdelegate">SpeedLimitDelegate</a>
  - <a href="sdk-for-ios-explore-structs-speedlimitoffset">SpeedLimitOffset</a>
  - <a href="sdk-for-ios-explore-protocols-speedwarningdelegate">SpeedWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-speedwarningoptions">SpeedWarningOptions</a>
  - <a href="sdk-for-ios-explore-enums-speedwarningstatus">SpeedWarningStatus</a>
  - <a href="sdk-for-ios-explore-enums-textnotificationtype">TextNotificationType</a>
  - <a href="sdk-for-ios-explore-enums-timingprofile">TimingProfile</a>
  - <a href="sdk-for-ios-explore-structs-tollbooth">TollBooth</a>
  - <a href="sdk-for-ios-explore-structs-tollboothlane">TollBoothLane</a>
  - <a href="sdk-for-ios-explore-enums-tollcollectionmethod">TollCollectionMethod</a>
  - <a href="sdk-for-ios-explore-structs-tollstop">TollStop</a>
  - <a href="sdk-for-ios-explore-protocols-tollstopwarningdelegate">TollStopWarningDelegate</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior">TrackingCameraBehavior</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-zoompolicy">– ZoomPolicy</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-speedthreshold">– SpeedThreshold</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-functionalroadclasszoompolicyoptions">– FunctionalRoadClassZoomPolicyOptions</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-speedbasedzoompolicyoptions">– SpeedBasedZoomPolicyOptions</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-maneuverzoomrange">– ManeuverZoomRange</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-maneuverruleoptions">– ManeuverRuleOptions</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-maneuverrule">– ManeuverRule</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-maneuvermodeconfiguration">– ManeuverModeConfiguration</a>
  - <a href="sdk-for-ios-explore-enums-trafficmergeroadtype">TrafficMergeRoadType</a>
  - <a href="sdk-for-ios-explore-enums-trafficmergeside">TrafficMergeSide</a>
  - <a href="sdk-for-ios-explore-structs-trafficmergewarning">TrafficMergeWarning</a>
  - <a href="sdk-for-ios-explore-protocols-trafficmergewarningdelegate">TrafficMergeWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-trafficmergewarningoptions">TrafficMergeWarningOptions</a>
  - <a href="sdk-for-ios-explore-structs-trafficonroutecolors">TrafficOnRouteColors</a>
  - <a href="sdk-for-ios-explore-structs-truckrestrictionwarning">TruckRestrictionWarning</a>
  - <a href="sdk-for-ios-explore-protocols-truckrestrictionswarningdelegate">TruckRestrictionsWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-truckrestrictionswarningoptions">TruckRestrictionsWarningOptions</a>
  - <a href="sdk-for-ios-explore-classes-visualnavigator">VisualNavigator</a>
  - <a href="sdk-for-ios-explore-classes-visualnavigatorcolors">VisualNavigatorColors</a>
  - <a href="sdk-for-ios-explore-protocols-wallclock">WallClock</a>
  - <a href="sdk-for-ios-explore-structs-warningnotificationdistances">WarningNotificationDistances</a>
  - <a href="sdk-for-ios-explore-enums-warningtype">WarningType</a>
  - <a href="sdk-for-ios-explore-enums-weathertype">WeatherType</a>
  - <a href="sdk-for-ios-explore-structs-weightrestriction">WeightRestriction</a>
  - <a href="sdk-for-ios-explore-enums-weightrestrictiontype">WeightRestrictionType</a>
- <a href="sdk-for-ios-explore-search">Search</a>
  - <a href="sdk-for-ios-explore-structs-address">Address</a>
  - <a href="sdk-for-ios-explore-enums-addresstype">AddressType</a>
  - <a href="sdk-for-ios-explore-structs-addressquery">AddressQuery</a>
  - <a href="sdk-for-ios-explore-enums-areatype">AreaType</a>
  - <a href="sdk-for-ios-explore-structs-businessdetails">BusinessDetails</a>
  - <a href="sdk-for-ios-explore-structs-categoryquery">CategoryQuery</a>
  - <a href="sdk-for-ios-explore-structs-categoryquery-area">– Area</a>
  - <a href="sdk-for-ios-explore-structs-contact">Contact</a>
  - <a href="sdk-for-ios-explore-structs-daterange">DateRange</a>
  - <a href="sdk-for-ios-explore-enums-dayofweek">DayOfWeek</a>
  - <a href="sdk-for-ios-explore-structs-details">Details</a>
  - <a href="sdk-for-ios-explore-structs-emailaddress">EmailAddress</a>
  - <a href="sdk-for-ios-explore-structs-emobilityserviceprovider">EMobilityServiceProvider</a>
  - <a href="sdk-for-ios-explore-structs-energymix">EnergyMix</a>
  - <a href="sdk-for-ios-explore-structs-energysource">EnergySource</a>
  - <a href="sdk-for-ios-explore-enums-energysourcetype">EnergySourceType</a>
  - <a href="sdk-for-ios-explore-structs-environmentalimpact">EnvironmentalImpact</a>
  - <a href="sdk-for-ios-explore-enums-environmentalimpactcategory">EnvironmentalImpactCategory</a>
  - <a href="sdk-for-ios-explore-enums-evaccessrestrictionreason">EVAccessRestrictionReason</a>
  - <a href="sdk-for-ios-explore-enums-evaccesstype">EVAccessType</a>
  - <a href="sdk-for-ios-explore-structs-evchargingconnector">EVChargingConnector</a>
  - <a href="sdk-for-ios-explore-structs-evchargingconnectorgroup">EVChargingConnectorGroup</a>
  - <a href="sdk-for-ios-explore-structs-evchargingconnectorreference">EVChargingConnectorReference</a>
  - <a href="sdk-for-ios-explore-structs-evchargingdurationrange">EVChargingDurationRange</a>
  - <a href="sdk-for-ios-explore-classes-evcharginglocation">EVChargingLocation</a>
  - <a href="sdk-for-ios-explore-enums-evcharginglocationfeature">EVChargingLocationFeature</a>
  - <a href="sdk-for-ios-explore-structs-evchargingopeninghours">EVChargingOpeningHours</a>
  - <a href="sdk-for-ios-explore-structs-evchargingopeninghoursexception">EVChargingOpeningHoursException</a>
  - <a href="sdk-for-ios-explore-structs-evchargingopeninghoursschedule">EVChargingOpeningHoursSchedule</a>
  - <a href="sdk-for-ios-explore-structs-evchargingoperator">EVChargingOperator</a>
  - <a href="sdk-for-ios-explore-structs-evchargingpooldetails">EVChargingPoolDetails</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtariff">EVChargingTariff</a>
  - <a href="sdk-for-ios-explore-enums-evchargingtariffdimension">EVChargingTariffDimension</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtariffelement">EVChargingTariffElement</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtariffelementcondition">EVChargingTariffElementCondition</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtariffpricecomponent">EVChargingTariffPriceComponent</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtariffrequest">EVChargingTariffRequest</a>
  - <a href="sdk-for-ios-explore-enums-evchargingtarifftype">EVChargingTariffType</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtruckrestriction">EVChargingTruckRestriction</a>
  - <a href="sdk-for-ios-explore-enums-evchargingvehiclecategory">EVChargingVehicleCategory</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk28EVCP3SearchCompletionHandlera">EVCP3SearchCompletionHandler</a>
  - <a href="sdk-for-ios-explore-structs-evse">Evse</a>
  - <a href="sdk-for-ios-explore-classes-evsearchengine">EVSearchEngine</a>
  - <a href="sdk-for-ios-explore-enums-evsearcherror">EVSearchError</a>
  - <a href="sdk-for-ios-explore-protocols-evsearchinterface">EVSearchInterface</a>
  - <a href="sdk-for-ios-explore-structs-evsearchoptions">EVSearchOptions</a>
  - <a href="sdk-for-ios-explore-structs-evseconnector">EVSEConnector</a>
  - <a href="sdk-for-ios-explore-structs-evseinfo">EVSEInfo</a>
  - <a href="sdk-for-ios-explore-enums-evsestatus">EVSEStatus</a>
  - <a href="sdk-for-ios-explore-enums-facilitytype">FacilityType</a>
  - <a href="sdk-for-ios-explore-structs-fueladditive">FuelAdditive</a>
  - <a href="sdk-for-ios-explore-enums-fueladditivetype">FuelAdditiveType</a>
  - <a href="sdk-for-ios-explore-structs-fuelstation">FuelStation</a>
  - <a href="sdk-for-ios-explore-enums-fueltype">FuelType</a>
  - <a href="sdk-for-ios-explore-structs-genericfuel">GenericFuel</a>
  - <a href="sdk-for-ios-explore-structs-geoplace">GeoPlace</a>
  - <a href="sdk-for-ios-explore-enums-highlighttype">HighlightType</a>
  - <a href="sdk-for-ios-explore-classes-indexrange">IndexRange</a>
  - <a href="sdk-for-ios-explore-structs-landlinephone">LandlinePhone</a>
  - <a href="sdk-for-ios-explore-structs-locationdetails">LocationDetails</a>
  - <a href="sdk-for-ios-explore-structs-mobilephone">MobilePhone</a>
  - <a href="sdk-for-ios-explore-classes-myplaces">MyPlaces</a>
  - <a href="sdk-for-ios-explore-classes-offlinesearchengine">OfflineSearchEngine</a>
  - <a href="sdk-for-ios-explore-classes-offlinesearchindex">OfflineSearchIndex</a>
  - <a href="sdk-for-ios-explore-classes-offlinesearchindex-operation">– Operation</a>
  - <a href="sdk-for-ios-explore-classes-offlinesearchindex-error">– Error</a>
  - <a href="sdk-for-ios-explore-classes-offlinesearchindex-options">– Options</a>
  - <a href="sdk-for-ios-explore-protocols-offlinesearchindexlistener">OfflineSearchIndexListener</a>
  - <a href="sdk-for-ios-explore-structs-openinghours">OpeningHours</a>
  - <a href="sdk-for-ios-explore-enums-parkingtype">ParkingType</a>
  - <a href="sdk-for-ios-explore-classes-place">Place</a>
  - <a href="sdk-for-ios-explore-classes-placecategory">PlaceCategory</a>
  - <a href="sdk-for-ios-explore-structs-placechain">PlaceChain</a>
  - <a href="sdk-for-ios-explore-structs-placefilter">PlaceFilter</a>
  - <a href="sdk-for-ios-explore-structs-placefilter-ev">– Ev</a>
  - <a href="sdk-for-ios-explore-structs-placefoodtype">PlaceFoodType</a>
  - <a href="sdk-for-ios-explore-structs-placeidquery">PlaceIdQuery</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk30PlaceIdSearchCompletionHandlera">PlaceIdSearchCompletionHandler</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk38PlaceIdSearchExtendedCompletionHandlera">PlaceIdSearchExtendedCompletionHandler</a>
  - <a href="sdk-for-ios-explore-enums-placeserializationerror">PlaceSerializationError</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk27PlaceSerializationExceptiona">PlaceSerializationException</a>
  - <a href="sdk-for-ios-explore-enums-placetype">PlaceType</a>
  - <a href="sdk-for-ios-explore-structs-poipaymentdetails">POIPaymentDetails</a>
  - <a href="sdk-for-ios-explore-structs-poipaymentmethod">POIPaymentMethod</a>
  - <a href="sdk-for-ios-explore-structs-responsedetails">ResponseDetails</a>
  - <a href="sdk-for-ios-explore-structs-scheduledetails">ScheduleDetails</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk31SearchExtendedCompletionHandlera">SearchExtendedCompletionHandler</a>
  - <a href="sdk-for-ios-explore-classes-searchengine">SearchEngine</a>
  - <a href="sdk-for-ios-explore-enums-searcherror">SearchError</a>
  - <a href="sdk-for-ios-explore-protocols-searchinterface">SearchInterface</a>
  - <a href="sdk-for-ios-explore-structs-searchoptions">SearchOptions</a>
  - <a href="sdk-for-ios-explore-structs-structuredquery">StructuredQuery</a>
  - <a href="sdk-for-ios-explore-structs-structuredquery-resulttype">– ResultType</a>
  - <a href="sdk-for-ios-explore-structs-structuredquery-addresselements">– AddressElements</a>
  - <a href="sdk-for-ios-explore-classes-suggestion">Suggestion</a>
  - <a href="sdk-for-ios-explore-enums-suggestiontype">SuggestionType</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk24SuggestCompletionHandlera">SuggestCompletionHandler</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk32SuggestExtendedCompletionHandlera">SuggestExtendedCompletionHandler</a>
  - <a href="sdk-for-ios-explore-structs-supplierreference">SupplierReference</a>
  - <a href="sdk-for-ios-explore-structs-textquery">TextQuery</a>
  - <a href="sdk-for-ios-explore-structs-textquery-area">– Area</a>
  - <a href="sdk-for-ios-explore-structs-timeofdayrange">TimeOfDayRange</a>
  - <a href="sdk-for-ios-explore-structs-truckamenities">TruckAmenities</a>
  - <a href="sdk-for-ios-explore-structs-truckfuel">TruckFuel</a>
  - <a href="sdk-for-ios-explore-structs-webdetails">WebDetails</a>
  - <a href="sdk-for-ios-explore-structs-webeditorial">WebEditorial</a>
  - <a href="sdk-for-ios-explore-structs-webimage">WebImage</a>
  - <a href="sdk-for-ios-explore-structs-webrating">WebRating</a>
  - <a href="sdk-for-ios-explore-structs-websiteaddress">WebsiteAddress</a>
  - <a href="sdk-for-ios-explore-structs-websource">WebSource</a>
  - <a href="sdk-for-ios-explore-classes-w3wsearchengine">W3WSearchEngine</a>
  - <a href="sdk-for-ios-explore-enums-w3wsearcherror">W3WSearchError</a>
  - <a href="sdk-for-ios-explore-structs-w3wsquare">W3WSquare</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk26W3WSearchCompletionHandlera">W3WSearchCompletionHandler</a>
- <a href="sdk-for-ios-explore-traffic">Traffic</a>
  - <a href="sdk-for-ios-explore-traffic#/s:7heresdk19TrafficDataProviderC">TrafficDataProvider</a>
  - <a href="sdk-for-ios-explore-classes-trafficengine">TrafficEngine</a>
  - <a href="sdk-for-ios-explore-classes-trafficflow">TrafficFlow</a>
  - <a href="sdk-for-ios-explore-protocols-trafficflowbase">TrafficFlowBase</a>
  - <a href="sdk-for-ios-explore-structs-trafficflowqueryoptions">TrafficFlowQueryOptions</a>
  - <a href="sdk-for-ios-explore-traffic#/s:7heresdk33TrafficFlowQueryCompletionHandlera">TrafficFlowQueryCompletionHandler</a>
  - <a href="sdk-for-ios-explore-classes-trafficincident">TrafficIncident</a>
  - <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory">– RestrictedVehicleCategory</a>
  - <a href="sdk-for-ios-explore-classes-trafficincident-vehiclerestriction">– VehicleRestriction</a>
  - <a href="sdk-for-ios-explore-protocols-trafficincidentbase">TrafficIncidentBase</a>
  - <a href="sdk-for-ios-explore-traffic#/s:7heresdk32TrafficIncidentCompletionHandlera">TrafficIncidentCompletionHandler</a>
  - <a href="sdk-for-ios-explore-enums-trafficincidentimpact">TrafficIncidentImpact</a>
  - <a href="sdk-for-ios-explore-structs-trafficincidentlookupoptions">TrafficIncidentLookupOptions</a>
  - <a href="sdk-for-ios-explore-classes-trafficincidentonroute">TrafficIncidentOnRoute</a>
  - <a href="sdk-for-ios-explore-enums-trafficincidenttype">TrafficIncidentType</a>
  - <a href="sdk-for-ios-explore-traffic#/s:7heresdk38TrafficIncidentsQueryCompletionHandlera">TrafficIncidentsQueryCompletionHandler</a>
  - <a href="sdk-for-ios-explore-structs-trafficincidentsqueryoptions">TrafficIncidentsQueryOptions</a>
  - <a href="sdk-for-ios-explore-structs-trafficlocation">TrafficLocation</a>
  - <a href="sdk-for-ios-explore-enums-trafficqueryerror">TrafficQueryError</a>
  - <a href="sdk-for-ios-explore-enums-traversability">Traversability</a>
- <a href="sdk-for-ios-explore-trafficradio">TrafficRadio</a>
  - <a href="sdk-for-ios-explore-classes-trafficbroadcast">TrafficBroadcast</a>
  - <a href="sdk-for-ios-explore-structs-trafficbroadcastparameters">TrafficBroadcastParameters</a>
  - <a href="sdk-for-ios-explore-structs-tmcdata">TMCData</a>
  - <a href="sdk-for-ios-explore-structs-tmcpreferredsidsrequest">TMCPreferredSidsRequest</a>
  - <a href="sdk-for-ios-explore-structs-tmcserviceproviderinfo">TMCServiceProviderInfo</a>
  - <a href="sdk-for-ios-explore-structs-tmcservicerequest">TMCServiceRequest</a>
  - <a href="sdk-for-ios-explore-protocols-tmcserviceinterface">TMCServiceInterface</a>
  - <a href="sdk-for-ios-explore-structs-rdsencryptionkey">RDSEncryptionKey</a>
  - <a href="sdk-for-ios-explore-structs-rdsencryptionkeysrequest">RDSEncryptionKeysRequest</a>
- <a href="sdk-for-ios-explore-transport">Transport</a>
  - <a href="sdk-for-ios-explore-structs-busspecifications">BusSpecifications</a>
  - <a href="sdk-for-ios-explore-structs-carspecifications">CarSpecifications</a>
  - <a href="sdk-for-ios-explore-structs-generalvehiclespeedlimits">GeneralVehicleSpeedLimits</a>
  - <a href="sdk-for-ios-explore-structs-hazardousmaterialrestriction">HazardousMaterialRestriction</a>
  - <a href="sdk-for-ios-explore-structs-pedestrianspecification">PedestrianSpecification</a>
  - <a href="sdk-for-ios-explore-enums-restrictiontype">RestrictionType</a>
  - <a href="sdk-for-ios-explore-structs-scooterspecification">ScooterSpecification</a>
  - <a href="sdk-for-ios-explore-structs-specificrestriction">SpecificRestriction</a>
  - <a href="sdk-for-ios-explore-structs-taxispecification">TaxiSpecification</a>
  - <a href="sdk-for-ios-explore-structs-timerestriction">TimeRestriction</a>
  - <a href="sdk-for-ios-explore-structs-timerestriction-category">– Category</a>
  - <a href="sdk-for-ios-explore-enums-transportmode">TransportMode</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification">TransportSpecification</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-carbuilder">– CarBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-truckbuilder">– TruckBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-pedestrianbuilder">– PedestrianBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-scooterbuilder">– ScooterBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-bicyclebuilder">– BicycleBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-taxibuilder">– TaxiBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-busbuilder">– BusBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-privatebusbuilder">– PrivateBusBuilder</a>
  - <a href="sdk-for-ios-explore-enums-transporttype">TransportType</a>
  - <a href="sdk-for-ios-explore-enums-truckcategory">TruckCategory</a>
  - <a href="sdk-for-ios-explore-enums-truckclass">TruckClass</a>
  - <a href="sdk-for-ios-explore-enums-truckroadtype">TruckRoadType</a>
  - <a href="sdk-for-ios-explore-enums-truckfueltype">TruckFuelType</a>
  - <a href="sdk-for-ios-explore-structs-vehiclerestriction">VehicleRestriction</a>
  - <a href="sdk-for-ios-explore-enums-vehicletype">VehicleType</a>
  - <a href="sdk-for-ios-explore-structs-vehicleprofile">VehicleProfile</a>
  - <a href="sdk-for-ios-explore-structs-weightperaxlegroup">WeightPerAxleGroup</a>
- <a href="sdk-for-ios-explore-venues">Venues</a>
  - <a href="sdk-for-ios-explore-classes-crosswalk">Crosswalk</a>
  - <a href="sdk-for-ios-explore-classes-crosswalk-classificationstyle">– ClassificationStyle</a>
  - <a href="sdk-for-ios-explore-classes-property">Property</a>
  - <a href="sdk-for-ios-explore-classes-property-propertytype">– PropertyType</a>
  - <a href="sdk-for-ios-explore-classes-venue">Venue</a>
  - <a href="sdk-for-ios-explore-protocols-venuedelegate">VenueDelegate</a>
  - <a href="sdk-for-ios-explore-classes-venuedrawing">VenueDrawing</a>
  - <a href="sdk-for-ios-explore-protocols-venuedrawingselectiondelegate">VenueDrawingSelectionDelegate</a>
  - <a href="sdk-for-ios-explore-classes-venueengine">VenueEngine</a>
  - <a href="sdk-for-ios-explore-venues#/s:7heresdk32VenueEngineInitCompletionHandlera">VenueEngineInitCompletionHandler</a>
  - <a href="sdk-for-ios-explore-venues#/s:7heresdk10VenueErrora">VenueError</a>
  - <a href="sdk-for-ios-explore-enums-venueerrorcode">VenueErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometry">VenueGeometry</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometry-internaladdress">– InternalAddress</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometry-geometrytype">– GeometryType</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometry-lookuptype">– LookupType</a>
  - <a href="sdk-for-ios-explore-enums-venuegeometryfiltertype">VenueGeometryFilterType</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometrystyle">VenueGeometryStyle</a>
  - <a href="sdk-for-ios-explore-classes-venueinfo">VenueInfo</a>
  - <a href="sdk-for-ios-explore-venues#/s:7heresdk17VenueInfoDataLista">VenueInfoDataList</a>
  - <a href="sdk-for-ios-explore-protocols-venueinfolistlistenerdelegate">VenueInfoListListenerDelegate</a>
  - <a href="sdk-for-ios-explore-classes-venuelabelstyle">VenueLabelStyle</a>
  - <a href="sdk-for-ios-explore-classes-venuelevel">VenueLevel</a>
  - <a href="sdk-for-ios-explore-protocols-venuelevelselectiondelegate">VenueLevelSelectionDelegate</a>
  - <a href="sdk-for-ios-explore-protocols-venuelifecycledelegate">VenueLifecycleDelegate</a>
  - <a href="sdk-for-ios-explore-venues#/s:7heresdk21VenueLoadErrorHandlera">VenueLoadErrorHandler</a>
  - <a href="sdk-for-ios-explore-classes-venuemap">VenueMap</a>
  - <a href="sdk-for-ios-explore-protocols-venuemapdelegate">VenueMapDelegate</a>
  - <a href="sdk-for-ios-explore-protocols-venuemaplifecycledelegate">VenueMapLifecycleDelegate</a>
  - <a href="sdk-for-ios-explore-classes-venuemodel">VenueModel</a>
  - <a href="sdk-for-ios-explore-protocols-venueselectiondelegate">VenueSelectionDelegate</a>
  - <a href="sdk-for-ios-explore-classes-venueservice">VenueService</a>
  - <a href="sdk-for-ios-explore-classes-venueservice-venueoptionalfeature">– VenueOptionalFeature</a>
  - <a href="sdk-for-ios-explore-protocols-venueservicedelegate">VenueServiceDelegate</a>
  - <a href="sdk-for-ios-explore-enums-venueserviceinitstatus">VenueServiceInitStatus</a>
  - <a href="sdk-for-ios-explore-classes-venuestyle">VenueStyle</a>
  - <a href="sdk-for-ios-explore-classes-venuetopology">VenueTopology</a>
  - <a href="sdk-for-ios-explore-classes-venuetopology-accesscharacteristics">– AccessCharacteristics</a>
  - <a href="sdk-for-ios-explore-classes-venuetopology-topologydirectionality">– TopologyDirectionality</a>
  - <a href="sdk-for-ios-explore-enums-venuetransportmode">VenueTransportMode</a>
  - <a href="sdk-for-ios-explore-enums-venuetransportmode-key">– Key</a>
  - <a href="sdk-for-ios-explore-enums-venuetransportmode-codingerror">– CodingError</a>
- <a href="sdk-for-ios-explore-warnerengine">WarnerEngine</a>
  - <a href="sdk-for-ios-explore-structs-customwarning">CustomWarning</a>
  - <a href="sdk-for-ios-explore-protocols-customwarningprovider">CustomWarningProvider</a>
  - <a href="sdk-for-ios-explore-structs-warning">Warning</a>
  - <a href="sdk-for-ios-explore-classes-warnerengine">WarnerEngine</a>
  - <a href="sdk-for-ios-explore-protocols-warningdelegate">WarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-warningoptions">WarningOptions</a>
  - <a href="sdk-for-ios-explore-classes-warningsregistry">WarningsRegistry</a>
- <a href="sdk-for-ios-explore-other%20classes">Other Classes</a>
  - <a href="sdk-for-ios-explore-classes-indoorsectiondetails">IndoorSectionDetails</a>
  - <a href="sdk-for-ios-explore-classes-locationmanager">LocationManager</a>
- <a href="sdk-for-ios-explore-other%20enums">Other Enumerations</a>
  - <a href="sdk-for-ios-explore-enums-commercialvehicleroadtype">CommercialVehicleRoadType</a>
  - <a href="sdk-for-ios-explore-enums-hazardousmaterialtype">HazardousMaterialType</a>
  - <a href="sdk-for-ios-explore-enums-indoorlevelchangefeatures">IndoorLevelChangeFeatures</a>
  - <a href="sdk-for-ios-explore-enums-indoormaneuveractions">IndoorManeuverActions</a>
  - <a href="sdk-for-ios-explore-enums-physicalstructure">PhysicalStructure</a>
  - <a href="sdk-for-ios-explore-enums-vehicletypecondition">VehicleTypeCondition</a>
- <a href="sdk-for-ios-explore-other%20functions">Other Functions</a>
  - <a href="sdk-for-ios-explore-other%20functions#/s:7heresdk24makeIOSPlatformThreadingAA08PlatformD0_pyF">makeIOSPlatformThreading()</a>
  - <a href="sdk-for-ios-explore-other%20functions#/s:7heresdk12synchronized_7closurexyp_xyXEtlF">synchronized(\_:closure:)</a>
- <a href="sdk-for-ios-explore-other%20protocols">Other Protocols</a>
  - <a href="sdk-for-ios-explore-protocols-matchedlocationlistener">MatchedLocationListener</a>
- <a href="sdk-for-ios-explore-other%20structs">Other Structures</a>
  - <a href="sdk-for-ios-explore-structs-admincontextid">AdminContextId</a>
  - <a href="sdk-for-ios-explore-structs-administrativecommercialvehiclerules">AdministrativeCommercialVehicleRules</a>
  - <a href="sdk-for-ios-explore-structs-driverestregulation">DriveRestRegulation</a>
  - <a href="sdk-for-ios-explore-structs-indoorlevelchangedata">IndoorLevelChangeData</a>
  - <a href="sdk-for-ios-explore-structs-indoorrouteplace">IndoorRoutePlace</a>
  - <a href="sdk-for-ios-explore-structs-indoorspacedata">IndoorSpaceData</a>
  - <a href="sdk-for-ios-explore-structs-lanedecreasewarning">LaneDecreaseWarning</a>
  - <a href="sdk-for-ios-explore-structs-lanedecreasewarningoptions">LaneDecreaseWarningOptions</a>
  - <a href="sdk-for-ios-explore-structs-refreshrouteparameters">RefreshRouteParameters</a>
  - <a href="sdk-for-ios-explore-structs-roadprofilecondition">RoadProfileCondition</a>
  - <a href="sdk-for-ios-explore-structs-vehicleprofilerestriction">VehicleProfileRestriction</a>
  - <a href="sdk-for-ios-explore-structs-vehiclerestrictioncondition">VehicleRestrictionCondition</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecificaccess">VehicleSpecificAccess</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecificspeedlimit">VehicleSpecificSpeedLimit</a>

</nav>

<article class="main-content">

<div class="section">

<div class="section section">

# MapData

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk19AdministrativeRulesV"></span>` `<span id="//apple_ref/swift/Struct/AdministrativeRules" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk19AdministrativeRulesV" class="token"><code>AdministrativeRules</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a set of administrative rules for a country or a state.

  <a href="sdk-for-ios-explore-structs-administrativerules" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct AdministrativeRules : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk25AdministrativeRulesLoaderC"></span>` `<span id="//apple_ref/swift/Class/AdministrativeRulesLoader" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk25AdministrativeRulesLoaderC" class="token"><code>AdministrativeRulesLoader</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides the protocol for the access to the administrative rules available for a country or a state in the local OCM map. Please be aware that the methods within this classload map data synchronously. In the event of absent data in the disk cache, the data will be retrieved from the remote server. To mitigate the potential freezing of the calling thread, it is advisable to proactively prefetch map data around the working area.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-administrativerulesloader" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class AdministrativeRulesLoader
  ```

  ``` highlight
  extension AdministrativeRulesLoader: NativeBase
  ```

  ``` highlight
  extension AdministrativeRulesLoader: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21AllowedTransportModesV"></span>` `<span id="//apple_ref/swift/Struct/AllowedTransportModes" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk21AllowedTransportModesV" class="token"><code>AllowedTransportModes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies which transport modes are allowed in a particular direction.

  **Note:** This struct specifies a general restriction to that transport mode, but additional restriction are possible.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-allowedtransportmodes" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct AllowedTransportModes : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24BloodAlcoholContentLimitV"></span>` `<span id="//apple_ref/swift/Struct/BloodAlcoholContentLimit" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk24BloodAlcoholContentLimitV" class="token"><code>BloodAlcoholContentLimit</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the rules regarding alcohol in blood content limit in a country or state for all types of drivers.

  <a href="sdk-for-ios-explore-structs-bloodalcoholcontentlimit" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct BloodAlcoholContentLimit : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12ConnectivityV"></span>` `<span id="//apple_ref/swift/Struct/Connectivity" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk12ConnectivityV" class="token"><code>Connectivity</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides information about link id and accessibility.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-connectivity" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Connectivity : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20DirectedOCMSegmentIdV"></span>` `<span id="//apple_ref/swift/Struct/DirectedOCMSegmentId" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk20DirectedOCMSegmentIdV" class="token"><code>DirectedOCMSegmentId</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  OCM Segment ID with travel direction of segment.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-directedocmsegmentid" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct DirectedOCMSegmentId : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22DownloadingFileOptionsV"></span>` `<span id="//apple_ref/swift/Struct/DownloadingFileOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk22DownloadingFileOptionsV" class="token"><code>DownloadingFileOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct which identifies the configuration when downloading a file reference.

  <a href="sdk-for-ios-explore-structs-downloadingfileoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct DownloadingFileOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11DrivingSideO"></span>` `<span id="//apple_ref/swift/Enum/DrivingSide" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk11DrivingSideO" class="token"><code>DrivingSide</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The side of the road on which the driving is done.

  <a href="sdk-for-ios-explore-enums-drivingside" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum DrivingSide : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13FileReferenceV"></span>` `<span id="//apple_ref/swift/Struct/FileReference" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk13FileReferenceV" class="token"><code>FileReference</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides information for a file reference.

  <a href="sdk-for-ios-explore-structs-filereference" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct FileReference : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17FileReferenceTypeO"></span>` `<span id="//apple_ref/swift/Enum/FileReferenceType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk17FileReferenceTypeO" class="token"><code>FileReferenceType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type of reference file.

  <a href="sdk-for-ios-explore-enums-filereferencetype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum FileReferenceType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21HeadlightsRequirementO"></span>` `<span id="//apple_ref/swift/Enum/HeadlightsRequirement" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk21HeadlightsRequirementO" class="token"><code>HeadlightsRequirement</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The situations in which headlights are required to be turned on.

  <a href="sdk-for-ios-explore-enums-headlightsrequirement" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum HeadlightsRequirement : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13LaneAttributeV"></span>` `<span id="//apple_ref/swift/Struct/LaneAttribute" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk13LaneAttributeV" class="token"><code>LaneAttribute</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that describes attributes assigned to a specific section of a lane. It includes lane markings, allowed travel directions, tolling info, access restrictions, and optional lane type.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-laneattribute" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LaneAttribute : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23LocalRoadCharacteristicO"></span>` `<span id="//apple_ref/swift/Enum/LocalRoadCharacteristic" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk23LocalRoadCharacteristicO" class="token"><code>LocalRoadCharacteristic</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the local road characteristics: frontage, parking lot road, poi access.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-localroadcharacteristic" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum LocalRoadCharacteristic : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18MapDataLoaderErrora"></span>` `<span id="//apple_ref/swift/Alias/MapDataLoaderError" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk18MapDataLoaderErrora" class="token"><code>MapDataLoaderError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Error occurred during obtaining data form the map. <a href="sdk-for-ios-explore-enums-mapdataloadererrorcode">`MapDataLoaderErrorCode`</a> represents possible errors.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias MapDataLoaderError = MapDataLoaderErrorCode
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22MapDataLoaderErrorCodeO"></span>` `<span id="//apple_ref/swift/Enum/MapDataLoaderErrorCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk22MapDataLoaderErrorCodeO" class="token"><code>MapDataLoaderErrorCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies possible errors from map data accessing.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-mapdataloadererrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum MapDataLoaderErrorCode : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension MapDataLoaderErrorCode : Error
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12OCMSegmentIdV"></span>` `<span id="//apple_ref/swift/Struct/OCMSegmentId" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk12OCMSegmentIdV" class="token"><code>OCMSegmentId</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  OCM Segment ID of particular matched <a href="sdk-for-ios-explore-structs-segmentreference">`SegmentReference`</a> from OCM map, represented in form: Tile + Local ID’s .

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-ocmsegmentid" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct OCMSegmentId : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21ParkingSideRegulationO"></span>` `<span id="//apple_ref/swift/Enum/ParkingSideRegulation" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk21ParkingSideRegulationO" class="token"><code>ParkingSideRegulation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The regulations for parking on the side of the road.

  <a href="sdk-for-ios-explore-enums-parkingsideregulation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ParkingSideRegulation : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18PhysicalAttributesV"></span>` `<span id="//apple_ref/swift/Struct/PhysicalAttributes" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk18PhysicalAttributesV" class="token"><code>PhysicalAttributes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Physical attributes of the segment.

  ***Note*** a road can have more than one attribute at the same time.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-physicalattributes" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct PhysicalAttributes : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15PreTripPlanningV"></span>` `<span id="//apple_ref/swift/Struct/PreTripPlanning" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk15PreTripPlanningV" class="token"><code>PreTripPlanning</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the legal requirements to be considered before a trip for all vehicles types.

  <a href="sdk-for-ios-explore-structs-pretripplanning" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct PreTripPlanning : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15RailwayCrossingV"></span>` `<span id="//apple_ref/swift/Struct/RailwayCrossing" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk15RailwayCrossingV" class="token"><code>RailwayCrossing</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifies the presence and the location of railway corssings. Included in <a href="sdk-for-ios-explore-classes-segmentdata">`SegmentData`</a> only if <a href="sdk-for-ios-explore-structs-segmentdataloaderoptions#/s:7heresdk24SegmentDataLoaderOptionsV20loadRailwayCrossingsSbvp">`SegmentDataLoaderOptions.loadRailwayCrossings`</a> is set to `true`.

  <a href="sdk-for-ios-explore-structs-railwaycrossing" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RailwayCrossing
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19RailwayCrossingTypeO"></span>` `<span id="//apple_ref/swift/Enum/RailwayCrossingType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk19RailwayCrossingTypeO" class="token"><code>RailwayCrossingType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type of railway crossing.

  <a href="sdk-for-ios-explore-enums-railwaycrossingtype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum RailwayCrossingType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11RoadDividerO"></span>` `<span id="//apple_ref/swift/Enum/RoadDivider" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk11RoadDividerO" class="token"><code>RoadDivider</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A physical structure or painted road marking intended to legally prohibit left turns in right-side driving countries, right turns in left-side driving countries, and U-turns at divided intersections or in the middle of divided segments.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-roaddivider" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum RoadDivider : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10RoadUsagesV"></span>` `<span id="//apple_ref/swift/Struct/RoadUsages" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk10RoadUsagesV" class="token"><code>RoadUsages</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Road Usages of the segment.

  ***Note*** a road can have more than one attribute at the same time.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-roadusages" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RoadUsages : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21SegmentConnectivitiesV"></span>` `<span id="//apple_ref/swift/Struct/SegmentConnectivities" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk21SegmentConnectivitiesV" class="token"><code>SegmentConnectivities</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides information about segment one direction source and target connectivities.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-segmentconnectivities" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SegmentConnectivities : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11SegmentDataC"></span>` `<span id="//apple_ref/swift/Class/SegmentData" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk11SegmentDataC" class="token"><code>SegmentData</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains the requested information for a segment

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-segmentdata" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SegmentData
  ```

  ``` highlight
  extension SegmentData: NativeBase
  ```

  ``` highlight
  extension SegmentData: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17SegmentDataLoaderC"></span>` `<span id="//apple_ref/swift/Class/SegmentDataLoader" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk17SegmentDataLoaderC" class="token"><code>SegmentDataLoader</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides the protocol for the access to the segments data available in the local OCM map. Please be aware that the methods within this class load map data synchronously. In the event of absent data in the disk cache, the data will be retrieved from the remote server. To mitigate the potential freezing of the calling thread, it is advisable to proactively prefetch map data around the working area.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-segmentdataloader" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SegmentDataLoader
  ```

  ``` highlight
  extension SegmentDataLoader: NativeBase
  ```

  ``` highlight
  extension SegmentDataLoader: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24SegmentDataLoaderOptionsV"></span>` `<span id="//apple_ref/swift/Struct/SegmentDataLoaderOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk24SegmentDataLoaderOptionsV" class="token"><code>SegmentDataLoaderOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies which data should be loaded by the

      SegmentDataLoader.loadData(...)

  or
      SegmentDataLoader.loadDirectedSegmentData(...)

  function.
  </p>

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-segmentdataloaderoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SegmentDataLoaderOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk25SegmentReferenceConverterC"></span>` `<span id="//apple_ref/swift/Class/SegmentReferenceConverter" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk25SegmentReferenceConverterC" class="token"><code>SegmentReferenceConverter</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A SegmentReferenceConverter provides possibility to convert mapmatched instances of <a href="sdk-for-ios-explore-structs-segmentreference">`SegmentReference`</a> to corresponding instances of <a href="sdk-for-ios-explore-structs-directedocmsegmentid">`DirectedOCMSegmentId`</a>.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-segmentreferenceconverter" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SegmentReferenceConverter
  ```

  ``` highlight
  extension SegmentReferenceConverter: NativeBase
  ```

  ``` highlight
  extension SegmentReferenceConverter: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15SegmentSpanDataC"></span>` `<span id="//apple_ref/swift/Class/SegmentSpanData" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk15SegmentSpanDataC" class="token"><code>SegmentSpanData</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains attributes that are not necessarily constant on a full segment. A Span is a portion of a Segment where the requested attributes are constant.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-segmentspandata" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SegmentSpanData
  ```

  ``` highlight
  extension SegmentSpanData: NativeBase
  ```

  ``` highlight
  extension SegmentSpanData: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk28SegmentSpecialSpeedSituationV"></span>` `<span id="//apple_ref/swift/Struct/SegmentSpecialSpeedSituation" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk28SegmentSpecialSpeedSituationV" class="token"><code>SegmentSpecialSpeedSituation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A special speed situation indicates a speed that exists under special circumstances. It can be used to further refine the estimation of traversal times, route calculation and calculation of route guidance timing.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-segmentspecialspeedsituation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SegmentSpecialSpeedSituation : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17SegmentSpeedLimitV"></span>` `<span id="//apple_ref/swift/Struct/SegmentSpeedLimit" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk17SegmentSpeedLimitV" class="token"><code>SegmentSpeedLimit</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes the posted speed limit on the segment span.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-segmentspeedlimit" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SegmentSpeedLimit : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16SpecialSpeedTypeO"></span>` `<span id="//apple_ref/swift/Enum/SpecialSpeedType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk16SpecialSpeedTypeO" class="token"><code>SpecialSpeedType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the speed situation type.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-specialspeedtype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum SpecialSpeedType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8TollCostV"></span>` `<span id="//apple_ref/swift/Struct/TollCost" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk8TollCostV" class="token"><code>TollCost</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains informations about the toll costs for a specific vehicle profile.

  <a href="sdk-for-ios-explore-structs-tollcost" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TollCost : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9TollPointV"></span>` `<span id="//apple_ref/swift/Struct/TollPoint" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk9TollPointV" class="token"><code>TollPoint</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct to represent the toll point attributes of a segment.

  <a href="sdk-for-ios-explore-structs-tollpoint" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TollPoint
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13TollStructureV"></span>` `<span id="//apple_ref/swift/Struct/TollStructure" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk13TollStructureV" class="token"><code>TollStructure</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that defines tolling configuration for a lane. It describes which types of toll structures apply and the acceptable payment methods. This information can be used to guide drivers through toll roads based on their preferences or vehicle capabilities.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-tollstructure" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TollStructure : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21TollStructureManeuverV"></span>` `<span id="//apple_ref/swift/Struct/TollStructureManeuver" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk21TollStructureManeuverV" class="token"><code>TollStructureManeuver</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides information for a toll structure at a toll point.

  <a href="sdk-for-ios-explore-structs-tollstructuremaneuver" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TollStructureManeuver
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17TollStructureTypeO"></span>` `<span id="//apple_ref/swift/Enum/TollStructureType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk17TollStructureTypeO" class="token"><code>TollStructureType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This enum defines the type of toll structure used on a road segment or lane. Each value represents a different tolling mechanism used in road infrastructure. This enum helps in providing detailed tolling information for routing and navigation.

  <a href="sdk-for-ios-explore-enums-tollstructuretype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TollStructureType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10TollSystemV"></span>` `<span id="//apple_ref/swift/Struct/TollSystem" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk10TollSystemV" class="token"><code>TollSystem</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains informations about a toll system.

  <a href="sdk-for-ios-explore-structs-tollsystem" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TollSystem : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13TrafficSignalV"></span>` `<span id="//apple_ref/swift/Struct/TrafficSignal" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk13TrafficSignalV" class="token"><code>TrafficSignal</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifies the presence and the location of traffic lights at an intersection

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-trafficsignal" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TrafficSignal
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21TrafficSignalLocationO"></span>` `<span id="//apple_ref/swift/Enum/TrafficSignalLocation" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk21TrafficSignalLocationO" class="token"><code>TrafficSignalLocation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the location of a traffic signal.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-trafficsignallocation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TrafficSignalLocation : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19TurnOnRedRegulationO"></span>` `<span id="//apple_ref/swift/Enum/TurnOnRedRegulation" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-mapdata#/s:7heresdk19TurnOnRedRegulationO" class="token"><code>TurnOnRedRegulation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The regulations for turning on the red color of the traffic light.

  <a href="sdk-for-ios-explore-enums-turnonredregulation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TurnOnRedRegulation : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 <a href="sdk-for-ios-explore" class="link" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

</div>

