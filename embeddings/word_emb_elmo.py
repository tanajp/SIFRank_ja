#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Sponge"
# Date: 2019/6/19
from allennlp.commands.elmo import ElmoEmbedder
import os
os.environ["CUDA_VISIBLE_DEVICES"] = '0'


class WordEmbeddings():
    """
        ELMo
        https://allennlp.org/elmo

    """

    def __init__(self, options_file='https://exawizardsallenlp.blob.core.windows.net/data/options.json', weight_file='/content/drive/My Drive/SIFRank_ja/auxiliary_data/weights.hdf5', cuda_device=0):
        self.cuda_device = cuda_device
        self.elmo = ElmoEmbedder(options_file, weight_file, cuda_device=self.cuda_device)

    def get_tokenized_words_embeddings(self, sents_tokened):
        """
        @see EmbeddingDistributor
        :param tokenized_sents: list of tokenized words string (sentences/phrases)
        :return: ndarray with shape (len(sents), dimension of embeddings)
        """

        elmo_embedding, elmo_mask = self.elmo.batch_to_embeddings(sents_tokened)
        if (self.cuda_device > -1):
            return elmo_embedding.cpu(), elmo_mask.cpu()
        else:
            return elmo_embedding, elmo_mask
