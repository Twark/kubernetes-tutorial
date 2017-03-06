metadata:
  Annotations: null
  ClusterName: ""
  CreationTimestamp: null
  DeletionGracePeriodSeconds: null
  DeletionTimestamp: null
  Finalizers: null
  GenerateName: ""
  Generation: 0
  Labels: null
  Name: mycluster.wavetesting.com
  Namespace: ""
  OwnerReferences: null
  ResourceVersion: ""
  SelfLink: ""
  UID: ""
spec:
  api:
    dns: {}
  channel: stable
  cloudProvider: aws
  clusterDNSDomain: cluster.local
  configBase: s3://kub-wavetesting-com-state-store/mycluster.wavetesting.com
  configStore: s3://kub-wavetesting-com-state-store/mycluster.wavetesting.com
  dnsZone: Z1367TPHY2LYGO
  docker:
    bridge: ""
    ipMasq: false
    ipTables: false
    logLevel: warn
    storage: overlay,aufs
    version: 1.12.3
  etcdClusters:
  - etcdMembers:
    - instanceGroup: master-eu-west-1a
      name: a
    name: main
  - etcdMembers:
    - instanceGroup: master-eu-west-1a
      name: a
    name: events
  keyStore: s3://kub-wavetesting-com-state-store/mycluster.wavetesting.com/pki
  kubeAPIServer:
    address: 127.0.0.1
    admissionControl:
    - NamespaceLifecycle
    - LimitRanger
    - ServiceAccount
    - PersistentVolumeLabel
    - DefaultStorageClass
    - ResourceQuota
    allowPrivileged: true
    anonymousAuth: false
    apiServerCount: 1
    basicAuthFile: /srv/kubernetes/basic_auth.csv
    clientCAFile: /srv/kubernetes/ca.crt
    cloudProvider: aws
    etcdServers:
    - http://127.0.0.1:4001
    etcdServersOverrides:
    - /events#http://127.0.0.1:4002
    image: gcr.io/google_containers/kube-apiserver:v1.5.2
    kubeletPreferredAddressTypes:
    - InternalIP
    - Hostname
    - ExternalIP
    - LegacyHostIP
    logLevel: 2
    pathSrvKubernetes: /srv/kubernetes
    pathSrvSshproxy: /srv/sshproxy
    securePort: 443
    serviceClusterIPRange: 100.64.0.0/13
    storageBackend: etcd2
    tlsCertFile: /srv/kubernetes/server.cert
    tlsPrivateKeyFile: /srv/kubernetes/server.key
    tokenAuthFile: /srv/kubernetes/known_tokens.csv
  kubeControllerManager:
    allocateNodeCIDRs: true
    attachDetachReconcileSyncPeriod: 1m0s
    cloudProvider: aws
    clusterCIDR: 100.96.0.0/11
    clusterName: mycluster.wavetesting.com
    configureCloudRoutes: true
    image: gcr.io/google_containers/kube-controller-manager:v1.5.2
    leaderElection:
      leaderElect: true
    logLevel: 2
    master: 127.0.0.1:8080
    pathSrvKubernetes: /srv/kubernetes
    rootCAFile: /srv/kubernetes/ca.crt
    serviceAccountPrivateKeyFile: /srv/kubernetes/server.key
  kubeDNS:
    domain: cluster.local
    image: gcr.io/google_containers/kubedns-amd64:1.3
    replicas: 2
    serverIP: 100.64.0.10
  kubeProxy:
    cpuRequest: 100m
    image: gcr.io/google_containers/kube-proxy:v1.5.2
    logLevel: 2
    master: https://api.internal.mycluster.wavetesting.com
  kubeScheduler:
    image: gcr.io/google_containers/kube-scheduler:v1.5.2
    leaderElection:
      leaderElect: true
    logLevel: 2
    master: 127.0.0.1:8080
  kubelet:
    allowPrivileged: true
    apiServers: https://api.internal.mycluster.wavetesting.com
    babysitDaemons: true
    cgroupRoot: docker
    cloudProvider: aws
    clusterDNS: 100.64.0.10
    clusterDomain: cluster.local
    enableDebuggingHandlers: true
    evictionHard: memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5%
    evictionPressureTransitionPeriod: 0s
    hostnameOverride: '@aws'
    logLevel: 2
    networkPluginMTU: 9001
    networkPluginName: kubenet
    nonMasqueradeCIDR: 100.64.0.0/10
    podManifestPath: /etc/kubernetes/manifests
  kubernetesApiAccess:
  - 0.0.0.0/0
  kubernetesVersion: 1.5.2
  masterInternalName: api.internal.mycluster.wavetesting.com
  masterKubelet:
    allowPrivileged: true
    apiServers: http://127.0.0.1:8080
    babysitDaemons: true
    cgroupRoot: docker
    cloudProvider: aws
    clusterDNS: 100.64.0.10
    clusterDomain: cluster.local
    enableDebuggingHandlers: true
    evictionHard: memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5%
    evictionPressureTransitionPeriod: 0s
    hostnameOverride: '@aws'
    logLevel: 2
    networkPluginMTU: 9001
    networkPluginName: kubenet
    nonMasqueradeCIDR: 100.64.0.0/10
    podManifestPath: /etc/kubernetes/manifests
    registerSchedulable: false
  masterPublicName: api.mycluster.wavetesting.com
  networkCIDR: 172.20.0.0/16
  networking:
    kubenet: {}
  nonMasqueradeCIDR: 100.64.0.0/10
  secretStore: s3://kub-wavetesting-com-state-store/mycluster.wavetesting.com/secrets
  serviceClusterIPRange: 100.64.0.0/13
  sshAccess:
  - 0.0.0.0/0
  subnets:
  - cidr: 172.20.32.0/19
    name: eu-west-1a
    type: Public
    zone: eu-west-1a
  topology:
    dns:
      type: Public
    masters: public
    nodes: public
