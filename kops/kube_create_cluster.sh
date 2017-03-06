export KOPS_STATE_STORE=s3://kub-wavetesting-com-state-store
kops create -f https://raw.githubusercontent.com/Twark/kubernetes-tutorial/master/kops/cluster_config
kops create -f https://raw.githubusercontent.com/Twark/kubernetes-tutorial/master/kops/master_config
kops create -f https://raw.githubusercontent.com/Twark/kubernetes-tutorial/master/kops/nodes_config
